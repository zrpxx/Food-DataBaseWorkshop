<template>
  <q-card>
    <q-img src="https://cdn.quasar.dev/img/chicken-salad.jpg"/>

    <q-card-section class="q-pt-none q-mt-xl" style="width: 400px">
      <div class="text-h4">
        Random food?
      </div>
      <div class="text-h5 text-grey">
        How about some {{ food_name }}?
      </div>
    </q-card-section>

    <q-separator/>

    <q-card-actions>
      <q-btn flat color="primary" @click="onCheck()">
        Check it out
      </q-btn>
    </q-card-actions>
  </q-card>
</template>

<script>
export default {
  name: "CardCafe",
  props: ['food_id', 'food_name'],
  methods: {
    onCheck() {
      this.$router.push({name: 'detail', params:{'food_id': this.food_id}})
    }
  }
}
</script>

<style scoped>

</style>
