<template>
  <v-app 
  class="rounded rounded-md"
  >
    <Header />

    <SidebarTest
    :caller="caller"
    :currentDisplayedImageID="currentDisplayedImageID"
    :pairList="pairList"
    @setCurrentDisplayedPair="(n: number) => currentDisplayedImageID = n"
    />

    <v-main class="flex align-center justify-center" style="min-height: 300px;">
      <ControlPanel 
      @loadNextPair="addImage"
      @changeDisplay="changeDisplay"
      @processCalib="processCalib"
      />
      <MainDisplay 
      :caller="caller"
      :currentDisplayedImageID="currentDisplayedImageID"
      :imageMetadata="imageMetadata"
      />
      <InfoPanel 
      :currentDisplayedImageID="currentDisplayedImageID"
      :pairList="pairList"
      v-if="currentDisplayedImageID>0"
      />
    </v-main>

  </v-app>
</template>



<script setup lang="ts">
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';
import { useToast } from 'vue-toastification';

import Caller from '@/utils/api';
import type { Pair, Metadata, Side } from '@/utils/datatypes';

const toast = useToast();

const currentDisplayedImageID = ref(0); //Default backend placeholder
const caller = new Caller();

const imageMetadata = ref<Record<string, Metadata>>({})
const pairList = ref<Pair[]>([]);
const selectedIdList = computed<number[]>(() => pairList.value.filter((pair) => pair.selected).map(a => a.id));


// functions
const WAITING_TIME = 300; //.3s 
let lastCall = 0;

function canBeExecuted(): boolean {
    const now = Date.now();
    if (now - lastCall < WAITING_TIME) {
        return false;
    }
    return true
}

async function addImage() {
  if (!canBeExecuted()){
    toast.error(`You're clicking too fast! Please wait ${WAITING_TIME/1000}s`);
    console.log("Clicking too fast !");
    return;
  }
  lastCall = Date.now();

  const existence = await caller.isNextAvailable()
  if (!existence.exists) {
    toast.error("Next pair is not available yet");
    console.log("Next pair is not available yet");
    return;
  }

  const nextPair = existence.imgId
  let selected: boolean = true 

  for (const side of ["left", "right"] as Side[]) {
    const metadata = await caller.getMetadata(side, nextPair);
    selected = selected && metadata.foundCorners;
    imageMetadata.value[caller.getImageUid(side, nextPair)] = metadata;
  }

  pairList.value.push(
    {id: nextPair, selected: selected}
  )
  
  currentDisplayedImageID.value = nextPair;
  console.log(`imported pair nb ${currentDisplayedImageID.value}`)
}

function changeDisplay(increment: number) {
  let currentIndex = pairList.value.findIndex(pair => pair.id === currentDisplayedImageID.value);

  if (currentIndex === -1) {
    return;
  }

  currentIndex += increment + pairList.value.length; //shift with len because somehow -1 % 5 = -1
  currentIndex %= pairList.value.length //warp increments

  currentDisplayedImageID.value = pairList.value[currentIndex].id

}
 
function toggleSelection() {
  const currentIndex = pairList.value.findIndex(pair => pair.id === currentDisplayedImageID.value);
  pairList.value[currentIndex].selected = !pairList.value[currentIndex].selected
}

function processCalib() {
  caller.processSelected(selectedIdList.value)
}

watch(selectedIdList, (newVal, oldVal) => {
  console.log(`Automatically relaunched a calibration`);
  processCalib();
});

// event handling
const handleKeydown = (event: KeyboardEvent) => {
  switch(event.key) { 
   case "n": case "N": { 
      addImage().then();
      break; 
   }
   case "ArrowLeft": case "ArrowDown": {
      changeDisplay(-1);
      break; 
   }
   case "ArrowRight": case "ArrowUp":{
      changeDisplay(1);
      break; 
   }
   case "Enter":{
      toggleSelection();
      break; 
   }
};
};


const isListenerAdded = ref(false); // Necessary when working w/ hot reload

onMounted(() => {
  if (!isListenerAdded.value) {
    window.addEventListener('keydown', handleKeydown);
    isListenerAdded.value = true;
  }
});

onUnmounted(() => {
  if (isListenerAdded.value) {
    window.removeEventListener('keydown', handleKeydown);
    isListenerAdded.value = false;
  }
});

</script>
