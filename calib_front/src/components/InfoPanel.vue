<template>
    <v-card 
    class="mx-auto my-8"
    elevation="16"
    max-width="90%"
    prepend-icon="mdi-information-outline"
    :title="`Pair ${props.currentDisplayedImageID}`"
    >
        <v-card-text class="bg-surface-light pt-4">
            <span>
                {{ props.pairList.find(pair => pair.id === props.currentDisplayedImageID) }}
            </span>
        </v-card-text>
    </v-card>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import type { Pair } from '@/utils/datatypes'

const props = defineProps({
    currentDisplayedImageID : {
        type: Number,
        required: true
    },
    pairList : {
        type: Array<Pair>,
        required: true
    }
})

const myMessage = ref('Hello World!')

</script>
