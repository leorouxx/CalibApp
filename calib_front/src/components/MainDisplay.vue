<template>
    <div class="image-container">
        <div class="image-sub-container">
            <img 
            :src="leftImageUrl" 
            class="img-photo" 
            :class="{'dark-img': darkImgStyle}"
            alt="No source">
            <div
                v-for="p in (leftPointsList ?? [])"
                class="point"
                :style="{
                    left: `${p.x / 6000 * 100}%`,
                    top: `${p.y / 4000 * 100}%`,
                }"
            >
            </div>
        </div>
        <div class="image-sub-container">
            <img 
            :src="rightImageUrl" 
            class="img-photo" 
            :class="{'dark-img': darkImgStyle}"
            alt="No source">
            <div
                v-for="p in (rightPointsList ?? [])"
                class="point"
                :style="{
                    left: `${p.x / 6000 * 100}%`,
                    top: `${p.y / 4000 * 100}%`,
                }"
            >
            </div>
        </div>
    </div>
</template>


<script setup lang="ts">
    import { computed } from 'vue';
    import type { PropType } from 'vue';
    import { useTheme } from 'vuetify';

    import Caller from '@/utils/api';
    import type { Metadata } from '@/utils/datatypes'

    const theme = useTheme();
    const props = defineProps({
        caller : {
            type: Caller,
            required: true
        },
        currentDisplayedImageID : {
            type: Number,
            required: true
        },
        imageMetadata : {
            type: Object as PropType<Record<string, Metadata>>,
            required: true
        }
    });

    const leftImageUrl = computed(() => props.caller.getImageUrl("left", props.currentDisplayedImageID, 'preview'));
    const rightImageUrl = computed(() => props.caller.getImageUrl("right", props.currentDisplayedImageID, 'preview'));

    const leftPointsList = computed(() => props?.imageMetadata?.[props.caller.getImageUid("left", props.currentDisplayedImageID)]?.corners)
    const rightPointsList = computed(() => props?.imageMetadata?.[props.caller.getImageUid("right", props.currentDisplayedImageID)]?.corners)

    const darkImgStyle = computed(() => (props.currentDisplayedImageID === 0) && theme.global.name.value === "dark")
</script>

<style scoped>
.image-container {
    position: relative;
    display: flex;
    justify-content:space-evenly;
    overflow: hidden;
}
.image-sub-container {
    position: relative;
    width: 50%;
    height: auto;
}
.img-photo {
    width: 100%;
    height: auto; /* Maintain aspect ratio */
    object-fit: contain;
    display: block;
    /* border: 3px solid black; */
}

.dark-img{
    filter: invert(100%);
}

.point {
  position: absolute;
  width: 10px;
  height: 10px;
  background-color: red;
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>