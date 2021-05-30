<template>
  <q-page class="q-pa-sm q-mx-xl q-mt-lg">
    <card-detail :food_id="food_id" :background_image="getBackground(food_score)" :food_score="food_score" :food_brand="food_brand" :food_name="food_name"
          :food_score_desc="food_score_desc" :energy="energy" :carbohydrate="carbohydrate" :sugar="sugar" :fat="fat" :protein="protein"></card-detail>
  </q-page>
</template>

<script>
import CardDetail from "components/cards/CardDetail";

export default {
  name: "Detail",
  components: {CardDetail},
  data () {
    return {
      loggedIn: false,
      food_id: 52222,
      food_name: '',
      food_brand: '',
      food_score: '',
      food_score_desc: '',
      carbohydrate: 0,
      sugar: 0,
      protein: 0,
      fat: 0,
      energy: 0,
      categories: [],
      background_img1:'linear-gradient(to top, #30cfd0 0%, #330867 100%)',
      background_img2:'linear-gradient(87deg, rgb(45, 206, 137), rgb(45, 206, 204)) !important',
      background_img3:'linear-gradient(137deg, rgb(250, 128, 114), rgb(148, 0, 213)) !important',
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
    if(this.$route.params.food_id !== undefined)
      this.food_id = this.$route.params.food_id
    let _this = this
    this.$axios.get('http://192.168.31.92:8000/api/product/' + this.food_id).then(function (response) {
      let res = response.data
      if(res.status === 'Success') {
        _this.food_name = res.food_name
        _this.food_brand = res.food_brand
        _this.food_score = res.food_score
        _this.food_score_desc = res.food_score_desc
        _this.carbohydrate = res.food_nutrition_carbohydrate
        _this.sugar = res.food_nutrition_sugar
        _this.protein = res.food_nutrition_protein
        _this.fat = res.food_nutrition_fat
        _this.energy = res.food_nutrition_energy_kcal
        _this.catagories = res.categories_name
        console.log(_this.catagories)
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
  },
  methods: {
    getBackground(food_score) {
      if(food_score === "A")
        return this.background_img2
      else if(food_score === "E")
        return this.background_img3
      return this.background_img1
    },
  }
}
</script>

<style scoped>

</style>
