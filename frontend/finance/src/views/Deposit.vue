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
            <v-card 
                class="mt-3"
                variant="outlined"
                color="white"
                rounded="lg">
                <v-card-text>
                    <h3>🏦은행을 선택하세요.</h3>
                    <v-chip-group
                        multiple
                        column
                        v-model=selection
                        selected-class="selected"
                    >
                        <v-chip
                            v-for="bank in banks"
                            :key="bank"
                            :text="bank"
                            variant="outlined"
                        ></v-chip>
                    </v-chip-group>
                </v-card-text>
            </v-card>
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

// 예금 검색 관련 은행 리스트
const banks = [
    'NH농협', '신한', '하나', '부산', '대구', 'SC제일', '수협', '제주', '카카오뱅크', 'KDB산업',
    '국민', '우리'
]
const selection = ref(null)
</script>

<style scoped>
h2 {
    color: white;
}
h2:hover {
    text-decoration: underline;
}
.searchIcon {
    stroke: white;
    stroke-width: 1;
}
.selected {
    background-color: white;
    color: #3F6387;
}
</style>