<template>
  <q-page class="flex flex-center" style="flex-flow: column">
    <div class="flex content-center">
      <p class="text-h1 text-primary">Search foods from our database </p>
    </div>
    <div class="q-my-xl content-center">
    <q-input rounded outlined v-model="search_name" label="Food name">
      <template v-slot:append>
        <q-icon name="search" @click="onSearch() "/>
      </template>
    </q-input>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "Search",
  data() {
    return {
      search_name: '',
      loggedIn: false
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
  },
  methods: {
    onSearch() {
      if(this.search_name === '')
      {
        this.$q.notify({
          type: 'negative',
          position: 'top',
          message: 'Please input something.'
        })
        return
      }
      let _this = this
      this.$axios.post('http://127.0.0.1:8000/api/search', {
        food_name: _this.search_name
      }).then(function (response) {
        console.log(response)
        let res = response.data.food_ids
        if(res.length === 0)
        {
          _this.$q.notify({
            type: 'negative',
            position: 'top',
            message: 'No matches.'
          })
        } else {
          _this.$router.push({
            name: 'detail',
            params: {
              food_id: res[0]
            }
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
}
</script>

<style scoped>

</style>
