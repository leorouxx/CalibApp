<template>
    <div class="control-container">
        <v-btn 
            color="green-lighten-1" 
            @mousedown.prevent 
            @click.stop="$emit('loadNextPair')" 
        >
            Load next pair (n)
        </v-btn>

        <v-btn 
            color="blue-lighten-1" 
            @mousedown.prevent 
            @click.stop="$emit('changeDisplay', -1)" 
        >
            <v-icon icon="mdi-chevron-left"></v-icon>
        </v-btn>

        <v-btn 
            color="blue-lighten-1" 
            @mousedown.prevent 
            @click.stop="$emit('changeDisplay', 1)"
        >
            <v-icon icon="mdi-chevron-right"></v-icon>
        </v-btn>

        <v-btn 
        color="red-lighten-1" 
        @mousedown.prevent 
        @click.stop="$emit('processCalib')" 
        class="btn-error">
            &lt/ Send Calib Request /&gt
        </v-btn>
    </div>
</template>

<script setup lang="ts">
defineEmits([
    'loadNextPair',
    'changeDisplay',
    'processCalib'
]);
</script>

<style scoped>
.control-container{
    padding: 1em;
    display: flex;
    justify-content: center;
    column-gap: 1em;
}
</style>