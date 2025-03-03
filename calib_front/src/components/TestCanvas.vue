<template>
    <div class="control_container">
        <button @click="imgID = Math.max(imgID - 1, 1)"> - </button>
        <button @click="imgID++"> + </button> 
        Image id: {{ imgID }}
    </div>
    <div class="image-container">
      <img :src="imageUrlLeft" alt="Unavailable Image">
      <img :src="imageUrlRight" alt="Unavailable Image">
    </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { getImageUrl } from '@/utils/api';

const imgID = ref(1);
const backendUrl = import.meta.env.VITE_BACKEND_URL;

const imageUrlLeft = computed(() => getImageUrl('left', imgID.value));
const imageUrlRight = computed(() => getImageUrl('right', imgID.value));

</script>

<style scoped>

.control_container {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 20px;
}

.image-container {
  display: flex;
  justify-content:space-evenly;
}

img {
  max-width: 45%; 
  height: auto; /* Maintain aspect ratio */
  object-fit: contain;
}

button {
  align-items: center;
  background-color: #0A66C2;
  border: 0;
  border-radius: 100px;
  box-sizing: border-box;
  color: #ffffff;
  cursor: pointer;
  display: inline-flex;
  font-family: -apple-system, system-ui, system-ui, "Segoe UI", Roboto, "Helvetica Neue", "Fira Sans", Ubuntu, Oxygen, "Oxygen Sans", Cantarell, "Droid Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Lucida Grande", Helvetica, Arial, sans-serif;
  font-size: 16px;
  font-weight: 600;
  justify-content: center;
  line-height: 20px;
  max-width: 480px;
  min-height: 40px;
  min-width: 0px;
  overflow: hidden;
  padding: 0px;
  padding-left: 20px;
  padding-right: 20px;
  text-align: center;
  touch-action: manipulation;
  transition: background-color 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s, box-shadow 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s, color 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s;
  user-select: none;
  -webkit-user-select: none;
  vertical-align: middle;
  margin-left: 10px;
  margin-right: 10px;
}

button:hover,
button:focus { 
  background-color: #16437E;
  color: #ffffff;
}

button:active {
  background: #09223b;
  color: rgb(255, 255, 255, .7);
}

button:disabled { 
  cursor: not-allowed;
  background: rgba(0, 0, 0, .08);
  color: rgba(0, 0, 0, .3);
}
</style>