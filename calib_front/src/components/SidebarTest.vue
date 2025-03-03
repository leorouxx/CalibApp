<template>
  <v-navigation-drawer
    width="260"
    :rail="rail"
    permanent
    @click="rail = false"
  >
    <v-list-item
      prepend-icon="mdi-history"
      title="Image History"
      nav
    >
      <template v-slot:append>
        <v-btn
          icon="mdi-chevron-left"
          variant="text"
          @click.stop="rail = !rail"
        ></v-btn>
      </template>
    </v-list-item>

    <v-divider></v-divider>

    <v-list v-if="!rail" density="comfortable" nav>
      <v-list-item
          v-for="pair in props.pairList.slice().reverse()" 
          :key="pair.id"
          class="border list-item-wrapper"
          :class="{displayed: (pair.id === currentDisplayedImageID)}"
          nav
          @click.stop="$emit('setCurrentDisplayedPair', pair.id)"
          >
            <div>
              <div class="list-item-text">
                  <div class="text-wrapper">
                    Pair # {{ pair.id }}
                  </div>
                  <v-checkbox-btn 
                    @mousedown.prevent 
                    @click.stop="pair.selected = !pair.selected" 
                    v-model="pair.selected" 
                    inline>
                  </v-checkbox-btn>
              </div>
              <div class="list-item-images">
                <img :src="caller.getImageUrl('left', pair.id, 'thumbnail')">
                <img :src="caller.getImageUrl('right', pair.id, 'thumbnail')">
              </div>
            </div>
          </v-list-item>
      </v-list>
  </v-navigation-drawer>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import type { Pair } from '@/utils/datatypes';
import Caller from '@/utils/api';

const rail = ref(false);

defineEmits(['setCurrentDisplayedPair'])


const props = defineProps<{
  caller: Caller;
  currentDisplayedImageID: number;
  pairList: Pair[]
}>();

const displaySelected = ref(true);
const displayUnselected = ref(true);
const displayAll = ref(true);

const toggleAll = () => {
    displaySelected.value = displayAll.value;
    displayUnselected.value = displayAll.value;
};

const updateAll = () => {
    displayAll.value = displaySelected.value && displayUnselected.value;
};

</script>

<style scoped>
.checkbox {
  margin-bottom: 4px;
}

.list-item-wrapper{
  padding-bottom: 1em;
  margin: .5em 0 .5em 0;
  background-color: rgba(154, 211, 220, 0.206);
}

.list-item-text {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    width: 100%;
}

.list-item-images{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 100%;
}

img {
  width: 45%;
  height: auto;
}

.displayed {
    background-color: #7ca1cf;
}
</style>