<template>
    <v-app-bar title="CalibWeb">
        <v-btn 
            rounded="xl" 
            @mousedown.prevent 
            @click.stop="toggleTheme" 
            class="theme-btn"
        >
            <v-icon :class="{ flip: isToggling }" size="32">
                {{ theme.global.current.value.dark ? 'mdi-weather-sunny' : 'mdi-weather-night' }}
            </v-icon>
        </v-btn>
    </v-app-bar>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useTheme } from 'vuetify'

const theme = useTheme()
const isToggling = ref(false)

function toggleTheme() {
    isToggling.value = true
    const duration = 300

    setTimeout(() => {
        theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
    }, duration/2)

    setTimeout(() => {
    isToggling.value = false
    }, duration/2)
};
</script>

<style scoped>
.theme-btn {
    font-size: 1.2rem; /* Make button text bigger */
}

.v-icon {
    transition: transform 0.3s ease-in-out, scale 0.3s ease-in-out;
}

.flip {
    transform: scaleX(-1); /* Flip horizontally */
}
</style>

