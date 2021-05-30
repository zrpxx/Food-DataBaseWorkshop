<template>
  <q-page class="q-pa-sm flex flex-center">
      <card-profile class="q-mx-lg" style="width: 20%;" :name="'Hello, ' + username" :des="isAdmin ? 'Administrator' : 'User'" :avatar="'https://cdn.quasar.dev/img/boy-avatar.png'"></card-profile>
      <CardCafe class="q-mx-lg" :food_id="random_food_id" :food_name="random_food_name"></CardCafe>
  </q-page>
</template>

<script>
export default {
  name: "PageIndex",
  components: {
    CardProfile: () => import('components/cards/CardProfile'),
    CardCafe: () => import('components/cards/CardCafe')
  },
  data() {
    return {
      loggedIn: true,
      username: '',
      isAdmin: false,
      random_food_name: '...',
      random_food_id: -1,
      background_img1:'linear-gradient(to top, #30cfd0 0%, #330867 100%)',
      background_img2:'linear-gradient(87deg, rgb(45, 206, 137), rgb(45, 206, 204)) !important'
    }
  },
  created() {
    this.loggedIn = sessionStorage.getItem('loggedIn') !== null
    if(!this.loggedIn && this.$router.path !== '/')
      this.$router.push('/')
    else {
      this.username = sessionStorage.getItem('loggedIn')
      console.log(this.username)
      this.isAdmin = sessionStorage.getItem('role') === '1'
    }
    let _this = this
    this.$axios.get('http://192.168.31.92:8000/api/random').then(function (response) {
      let res = response.data
      if(res.status === 'Success') {
        _this.random_food_id = res.food_id
        _this.random_food_name = res.food_name
      } else {
        _this.$q.notify({
          type: 'negative',
          message: 'Loading failed.'
        })
      }
    }).catch(function (error) {
      console.log(error)
      _this.$q.notify({
        type: 'negative',
        position: 'top',
        message: 'Internal error.'
      })
    })
  }
}
</script>

<style scoped>

</style>
