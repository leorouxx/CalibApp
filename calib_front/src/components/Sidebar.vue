<template>
    <v-navigation-drawer>
        <div class="d-flex flex-column">
            <span>View:</span>
            <v-checkbox-btn v-model="displayAll" label="All" @change="toggleAll" class="checkbox"></v-checkbox-btn>
            <v-checkbox-btn v-model="displaySelected" label="Selected" @change="updateAll" class="checkbox"></v-checkbox-btn>
            <v-checkbox-btn v-model="displayUnselected" label="Unselected" @change="updateAll" class="checkbox"></v-checkbox-btn>
        </div>

        <v-list>
            <v-list-item
            v-for="pair in props.pairList.slice().reverse()" 
            :key="pair.id"
            class="border"
            :class="{selected: pair.selected}"
            >
            <div class="custom-list-item-content">
                <div class="text-wrapper">
                    {{ pair.id }}
                </div>
                <v-checkbox-btn v-model="pair.selected" inline></v-checkbox-btn>
            </div>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>


<script setup lang="ts">
import { ref } from 'vue';
import type { Pair } from '@/utils/datatypes';

const props = defineProps({
    pairList : {
        type: Array<Pair>,
        required: true
    }
    });

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
.custom-list-item-content {
    background-color: blue;
}


.selected {
    background-color: rgb(164, 239, 252);
}
</style>