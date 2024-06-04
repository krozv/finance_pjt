<template>
    <div class="mx-16 mt-4">
        <h2>환율 계산기를 사용해보세요.</h2>
        <v-row class="mt-1">
            <v-col cols="12">
                <CountryComponent 
                v-if="!selected"
                @selected="from"/>
                <ValueComponent
                :selected-country="selectedCountry"
                v-else />
            </v-col>
        </v-row>
    </div>
</template>

<script setup>
import CountryComponent from '@/components/CountryComponent.vue'
import ValueComponent from '@/components/ValueComponent.vue'
import { ref } from 'vue'
const selectedCountry = ref(null)
const selected = ref(false)
const from = function(country) {
    selectedCountry.value = country
    selected.value= true
}
</script>

<style scoped>
h2 {
    color: white
}

.arrow {
    color: white;
    font-size: xx-large;
}
</style>