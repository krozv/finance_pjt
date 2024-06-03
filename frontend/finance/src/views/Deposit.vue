<template>
    <div class="mx-16 mt-4">
        <h2>예금 상품을 찾아보세요.</h2>
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

// 추후 django 연결해서 예금 리스트 불러올 예정
const items = [
    {title: '예금1', bank: '기업은행'},
    {title: '예금1', bank: '기업은행'},
    {title: '예금1', bank: '기업은행'},
    {title: '예금1', bank: '기업은행'},
    {title: '예금1', bank: '기업은행'},
    {title: '예금1', bank: '기업은행'},
]
</script>

<style scoped>
h2 {
    color: white
}
</style>