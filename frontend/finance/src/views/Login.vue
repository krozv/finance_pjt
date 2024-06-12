<template>
    <v-card class="mx-auto mt-10" max-width="350" title="로그인을 해주세요.">
        <v-container>
            <v-text-field
            v-model="email"
            :rules="[required]"
            label="Email"
            placeholder="Enter your email"
            clearable
            ></v-text-field>
            <v-text-field
            v-model="password"
            :rules="[required]"
            label="Password"
            placeholder="Enter your password"
            clearable
            ></v-text-field>
        </v-container>
        <v-divider></v-divider>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
            type="submit"
            @click="login">
                Log In
            </v-btn>
        </v-card-actions>
    </v-card>
    <div class="signin mt-2 mx-auto d-flex justify-center">
        <p @click="moveTo">회원가입</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const required = function (v) {
    return !!v || 'Field is required'
}

const email = ref(null)
const password = ref(null)

const router = useRouter()
// 로그인 보내기
const login = function () {

}

// 회원가입 페이지
const moveTo = function () {
    router.push({ name: 'signin' })
}
</script>

<style scoped>
.signin {
    color: white;
}
.signin:hover {
    text-decoration: underline;
}
</style>