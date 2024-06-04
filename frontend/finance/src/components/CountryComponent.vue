<template>
    <v-card
        variant="outlined"
        color="white">
        
        <v-card-text>
            <div v-if="selectedCountry && selectedCountry.length > 0">
                    <div class="d-flex">
                        <div class="d-flex">
                        <h3>
                        From: {{ selectedCountry[0] }}
                        </h3>
                        <h3>
                            &nbsp;→&nbsp;
                        </h3>
                        <h3 v-if="selectedCountry[1]">
                            To: {{ selectedCountry[1] }}
                        </h3>
                        </div>
                        <v-spacer></v-spacer>
                        <v-btn v-if="selectedCountry[1]"
                        size="small"
                        rounded="xl"
                        @click="$emit('selected', selectedCountry)"
                        >환율 계산</v-btn>
                        </div>
                    </div>
                <h3 v-else>국가를 선택해주세요.</h3>
            <v-chip-group
                v-model="selectedCountry"
                selected-class="selected"
                column multiple>
                
                <div class="mt-3">
                <v-chip
                    v-for="country in countries"
                    :key="country"
                    :text="country"
                    :value="country"
                ></v-chip>
                </div>
            </v-chip-group>
        </v-card-text>
        
    </v-card>
    
</template>

<script setup>
import { ref } from 'vue'
const selectedCountry = ref(null)
const emits = defineEmits(['selected'])
const countries = [
    '🇦🇪 아랍에미리트',
    '🇦🇹 오스트리아',
    '🇦🇺 호주',
    '🇧🇪 벨기에',
    '🇧🇭 바레인',
    '🇨🇦 캐나다',
    '🇨🇭 스위스',
    '🇨🇳 중국',
    '🇩🇪 독일',
    '🇩🇰 덴마크',
    '🇪🇸 스페인',
    '🇪🇺 EU',
    '🇫🇮 핀란드',
    '🇫🇷 프랑스',
    '🇬🇧 영국',
    '🇭🇰 홍콩',
    '🇮🇩 인도네시아',
    '🇮🇹 이탈리아',
    '🇯🇵 일본',
    '🇰🇷 한국',
    '🇰🇼 쿠웨이트',
    '🇲🇾 말레이시아',
    '🇳🇱 네덜란드',
    '🇳🇴 노르웨이',
    '🇳🇿 뉴질랜드',
    '🇸🇦 사우디아라비아',
    '🇸🇪 스웨덴',
    '🇸🇬 싱가포르',
    '🇹🇭 태국',
    '🇺🇸 미국',
]
</script>

<style scoped>
.selected {
    background-color: white;
    color: #3F6387;
}
.test {
    justify-self: space-between;
}
</style>