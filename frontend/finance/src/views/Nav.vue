<template>
    <v-toolbar color='#0D151D' class="px-16 nav">
        <v-btn 
        @click="moveTo('home')" 
        :class="{ active: activeButton === 'home' }">
            서비스명
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn 
        @click="moveTo('deposit')"
        :class="{ active: activeButton === 'deposit' }">
            예금
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn 
        @click="moveTo('savings')"
        :class="{ active: activeButton === 'savings' }">
            적금
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn 
        @click="moveTo('exchange')"
        :class="{ active: activeButton === 'exchange' }">
            환율
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn 
        @click="moveTo('myPage')"
        :class="{ active: activeButton === 'myPage' }">
            마이페이지
        </v-btn>
    </v-toolbar>
    <router-view></router-view>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
const router = useRouter()

// click 상태 확인
const activeButton = ref(false)

// router 이동
const moveTo = function (name) {
    activeButton.value = name
    router.push({ name: name })
}

</script>

<style scoped>
.active {
    text-decoration: underline;
}

.nav {
    opacity: 0.9;
}
</style>