<template>
  <q-card>
    <q-card-section class="text-center">
      <q-avatar size="100px" class="shadow-10">
        <img :src="avatar">
      </q-avatar>
    </q-card-section>

    <q-card-section class="q-pt-none text-center ">
      <div class="text-h3  text-grey-8">
        {{ name }}
      </div>
      <div class="text-subtitle1 text-grey-8">
        {{ des }}
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: "CardProfile",
  props: ['avatar', 'name', 'des']
}
</script>

<style scoped>

</style>
