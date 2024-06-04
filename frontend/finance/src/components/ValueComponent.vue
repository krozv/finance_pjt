<template>
    <v-card
        variant="outlined"
        color="white">
        <v-card-text>
            <div class="d-flex">
            <h3>{{ selectedCountry[0] }}:</h3>
            <v-text-field></v-text-field>
            </div>
            <div class="d-flex">
                <h3>{{ selectedCountry[1] }}:</h3>
            </div>
        </v-card-text>
    </v-card>
</template>

<script setup>
const props = defineProps({
    selectedCountry: Object
})
</script>

<style scoped>

</style>