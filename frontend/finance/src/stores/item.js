import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useItemStore = defineStore('item', () => {
  const item = ref(null)

  const setItem = function (newItem) {
    item.value = newItem
    localStorage.setItem('item', JSON.stringify(newItem))
  }
  const clearItem = function () {
    item.value = null
    localStorage.removeItem('item')
  }
  // 초기화 시 localStorage에 저장된 데이터 가져와서 상태 복원
  // 필요한 지 의문. 확인해볼것.
  const restoreFromLocalStorage = function () {
    const savedItem = localStorage.getItem('item')
    if (savedItem) {
        item.value = JSON.parse(savedItem)
    }
  }
  return { item, setItem, clearItem, restoreFromLocalStorage }
})
