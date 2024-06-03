<template>
    <div class="mx-16 mt-4">
        <h2 
            class="d-flex align-items-center"
            @click="showSearch = !showSearch"
        >
            <svg-icon type="mdi" :path="mdilMagnify"
            class="searchIcon align-self-center mb-1"></svg-icon>
            예금 상품을 찾아보세요.
        </h2>
        <div v-if="showSearch">
            <v-text-field
                label="Search"
                prepend-inner-icon="mdi-magnify"
            ></v-text-field>
        </div>
        <v-row class="mt-1">
            <v-col cols="4"
                v-for="item in items">
                    <DepositComponent :item=item>
                    </DepositComponent>
            </v-col>
        </v-row>
    </div>
</template>

<script setup>
import DepositComponent from '@/components/DepositComponent.vue'
import SvgIcon from '@jamescoyle/vue-icon';
import { mdilMagnify } from '@mdi/light-js';
import { ref } from 'vue'

// 추후 django 연결해서 예금 리스트 불러올 예정
const items = [
    {title: '예금1', bank: '기업은행'},
    {title: '예금1', bank: '기업은행'},
    {title: '예금1', bank: '기업은행'},
    {title: '예금1', bank: '기업은행'},
    {title: '예금1', bank: '기업은행'},
    {title: '예금1', bank: '기업은행'},
]
// 예금 검색 기능 추가 예정
const showSearch = ref(false)
</script>

<style scoped>
h2 {
    color: white
}
h2:hover{
    text-decoration: underline;
}
.searchIcon {
    stroke: white;
    stroke-width: 1;
}
</style>