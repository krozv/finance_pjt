<template>
    <v-card
        variant="outlined"
        color="white">
        <v-card-text>
            <div class="d-flex align-center justify-space-between">
                <h3>{{ selectedCountry[0] }}:</h3>
                <div class="d-flex">
                <input type="number" v-model="from" class="from">
                <h3>단위</h3>
                </div>
            </div>
            <div class="d-flex align-center mt-3 justify-space-between">
                <h3>{{ selectedCountry[1] }}:</h3>
                <div class="d-flex">
                <input type="number" v-model="to" class="to">
                <h3>단위</h3>
                </div>
            </div>
            <div class="d-flex justify-end">
                <v-btn size="small"
                rounded="xl"
                class=mt-2
                @click="calculate">계산</v-btn>
            </div>
        </v-card-text>
    </v-card>
</template>

<script setup>
import { ref } from 'vue'
const props = defineProps({
    selectedCountry: Object
})
const from = ref(0)
const to = ref(0)

// 환율 계산하는 함수 작성하기
const calculate = function () {

}
</script>

<style scoped>
.from {
    text-align: end;
    font-weight: bold;
    color: white;
}
.to {
    text-align: end;
    color: white;
    font-weight: bold;
}
</style>