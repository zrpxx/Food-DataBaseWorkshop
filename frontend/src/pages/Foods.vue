<template>
    <q-page class="q-pa-sm">
        <div ref="scrollTarget" class="row q-col-gutter-lg" style="overflow: scroll; max-height: 1000px">
          <div class="col-lg-4 col-md-4 col-xs-12 col-sm-12">
            <q-infinite-scroll @load="onLoad" :offset="50" :scroll-target="$refs.scrollTarget">
            <card-company v-for="food in foods[0]" v-bind:key="food.id" class="q-mt-lg" :background_image="getBackground(food.score)" :food_id="food.id" :food_name="food.name" :food_brand="food.brand" :food_score="food.score" :food_category="food.categories"></card-company>
              <template v-slot:loading>
                <div class="row justify-center q-my-md">
                  <q-spinner-dots color="primary" size="40px" />
                </div>
              </template>
            </q-infinite-scroll>
          </div>
          <div class="col-lg-4 col-md-4 col-xs-12 col-sm-12">
            <card-company v-for="food in foods[1]" v-bind:key="food.id" class="q-mt-lg" :background_image="getBackground(food.score)" :food_id="food.id" :food_name="food.name" :food_brand="food.brand" :food_score="food.score" :food_category="food.categories"></card-company>
          </div>
          <div class="col-lg-4 col-md-4 col-xs-12 col-sm-12">
            <card-company v-for="food in foods[2]" v-bind:key="food.id" class="q-mt-lg" :background_image="getBackground(food.score)" :food_id="food.id" :food_name="food.name" :food_brand="food.brand" :food_score="food.score" :food_category="food.categories"></card-company>
          </div>
        </div>
    </q-page>
</template>

<script>
export default {
  name: "foods",
  components: {
    CardCompany: () => import('components/cards/CardCompany')
  },
  data() {
    return {
      loggedIn: false,
      background_img1:'linear-gradient(to top, #30cfd0 0%, #330867 100%)',
      background_img2:'linear-gradient(87deg, rgb(45, 206, 137), rgb(45, 206, 204)) !important',
      background_img3:'linear-gradient(137deg, rgb(250, 128, 114), rgb(148, 0, 213)) !important',
      foods: [[], [], []]
    }
  },
  created() {
    this.loggedIn = sessionStorage.getItem('loggedIn') !== null
    if(!this.loggedIn && this.$router.path !== '/')
      this.$router.push('/')
    else {
      this.username = sessionStorage.getItem('loggedIn')
      this.isAdmin = sessionStorage.getItem('role') === '1'
    }
    let _this = this
    this.$axios.get('http://127.0.0.1:8000/api/query/1').then(function (response) {
      let res = response.data;
      //console.log(res)
      for(let i = 0; i < res.food_id.length; i++) {
        let food = {}
        food.id = res.food_id[i]
        food.brand = res.food_brand[i]
        food.categories = res.food_categories[i]
        food.score = res.food_score[i]
        food.name = res.food_name[i]
        _this.foods[i % 3].push(food)
      }
      console.log(_this.foods)
    }).catch(function (error) {
      console.log(error)
      this.$q.notify({
        type: 'negative',
        message: 'Internal error.',
        position: 'top'
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
    onLoad(index, done) {
      setTimeout(() => {
        let _this = this
        this.$axios.get('http://127.0.0.1:8000/api/query/' + (_this.foods[0].length + this.foods[1].length + this.foods[2].length)).then(function (response) {
          let res = response.data;
          //console.log(res)
          for(let i = 0; i < res.food_id.length; i++) {
            let food = {}
            food.id = res.food_id[i]
            food.brand = res.food_brand[i]
            food.categories = res.food_categories[i]
            food.score = res.food_score[i]
            food.name = res.food_name[i]
            _this.foods[i % 3].push(food)
          }
          console.log(_this.foods)
        }).catch(function (error) {
          console.log(error)
          _this.$q.notify({
            type: 'negative',
            message: 'Internal error.',
            position: 'top'
          })
        })
        done()
      }, 2000)
    }
  }
}
</script>

<style scoped>

</style>
