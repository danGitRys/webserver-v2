import { defineStore } from "pinia";

export const testStore = defineStore('test',{
  state:() => ({
    test: 'test',
  }),
  actions:{
    set(message){
      this.test = message
    }
  }
})