<template>
  <div>
    <q-card class="text-white" :style="{'background-image': background_image}">
      <q-card-section>
        <br>
        <div class="text-h1 text-weight-bolder text-center">
          {{ food_name }}
        </div>
        <br>
      </q-card-section>
      <q-separator/>
      <q-card-section>
        <div class="text-h2 text-weight-bolder text-center">
          <q-icon name="restaurant_menu"></q-icon>
        </div>
      </q-card-section>
      <q-card-section class="q-pa-none">
        <div class="text-h2 text-weight-bolder text-center">
          Rank: {{ food_score }}
        </div>
        <div class="text-h2 text-center">
          {{ food_score_desc }}
        </div>
      </q-card-section>
      <br>
      <q-card-section>
        <div class="text-h2 text-weight-bolder text-center">
          Brand: {{ food_brand }}
        </div>
      </q-card-section>
      <br>
      <q-card-section>
        <div class="text-h2 text-weight-bolder text-center">
            Nutrition
        </div>
      </q-card-section>
      <q-card-section>
        <div class="text-h3 text-center q-mb-md">
          <div style="display: inline">
             Energy: {{ energy }} KCal / 100g
            <q-linear-progress stripe rounded size="20px" :value="energy / 600" color="warning" class="q-mt-sm" />
          </div>
        </div>
        <div class="text-h3 text-center q-mb-md">
          <div style="display: inline">
            Carbohydrate: {{ carbohydrate }} g / 100g
            <q-linear-progress stripe rounded size="20px" :value="carbohydrate / 100" color="warning" class="q-mt-sm" />
          </div>
        </div>
        <div class="text-h3 text-center q-mb-md">
          <div style="display: inline">
            Sugar: {{ sugar }} g / 100g
            <q-linear-progress stripe rounded size="20px" :value="sugar / 100" color="warning" class="q-mt-sm" />
          </div>
        </div>
        <div class="text-h3 text-center q-mb-md">
          <div style="display: inline">
            Protein: {{ protein }} g / 100g
            <q-linear-progress stripe rounded size="20px" :value="protein / 100" color="warning" class="q-mt-sm" />
          </div>
        </div>
        <div class="text-h3 text-center q-mb-md">
          <div style="display: inline">
            Fat: {{ fat }} g / 100g
            <q-linear-progress stripe rounded size="20px" :value="fat / 100" color="warning" class="q-mt-sm" />
          </div>
        </div>
      </q-card-section>
      <br>
      <q-separator/>
      <q-card-section class="text-center" v-if="isAdmin">
        <div class="text-h3 text-center q-mb-md">
          Administrate*
        </div>
        <q-btn label="Edit" color="primary" class="q-mx-xl" @click="onEdit()"></q-btn>
        <q-btn label="Delete" color="red" class="q-mx-xl" @click="deleteConfirm = true"></q-btn>
      </q-card-section>
    </q-card>
    <q-dialog v-model="deleteConfirm" persistent>
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="signal_wifi_off" color="primary" text-color="white" />
          <span class="q-ml-sm">Are you sure to delete this food?</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="primary" v-close-popup/>
          <q-btn flat label="Delete anyway" color="red" v-close-popup @click="onDelete()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="editForm" persistent>
      <q-card>
        <q-form
          @submit="onSubmit"
          class="q-gutter-md"
        >
          <q-input
            filled
            disable
            v-model="new_name"
            label="Food name *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please type something']"
          />

          <q-input
            filled
            v-model="new_brand"
            disable
            label="Brand name *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please type something']"
          />

          <q-select v-model="new_score" :options="score_options" label="New score" />

          <q-input
            filled
            type="number"
            v-model="new_energy"
            label="New energy *"
            lazy-rules
            :rules="[
          val => val !== null && val !== '' || 'Please type a energy',
          val => val > 0 || 'Please type a positive energy'
        ]"
          />

          <q-input
            filled
            type="number"
            v-model="new_carbohydrate"
            label="New carbohydrate *"
            lazy-rules
            :rules="[
          val => val !== null && val !== '' || 'Please type a new_carbohydrate',
          val => val > 0 || 'Please type a positive new_carbohydrate'
        ]"
          />

          <q-input
            filled
            type="number"
            v-model="new_sugar"
            label="New sugar *"
            lazy-rules
            :rules="[
          val => val !== null && val !== '' || 'Please type a sugar',
          val => val > 0 || 'Please type a positive sugar'
        ]"
          />

          <q-input
            filled
            type="number"
            v-model="new_fat"
            label="New fat *"
            lazy-rules
            :rules="[
          val => val !== null && val !== '' || 'Please type a fat',
          val => val > 0 || 'Please type a positive fat'
        ]"
          />

          <q-input
            filled
            type="number"
            v-model="new_protein"
            label="New protein *"
            lazy-rules
            :rules="[
          val => val !== null && val !== '' || 'Please type a protein',
          val => val > 0 || 'Please type a positive protein'
        ]"
          />

          <div>
            <q-btn label="Submit" type="submit" color="primary"/>
            <q-btn flat label="Cancel" color="primary" v-close-popup />
          </div>
        </q-form>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: "CardDetail",
  props:['background_image', 'food_name', 'food_id', 'food_brand', 'food_score', 'food_score_desc', 'energy', 'carbohydrate', 'sugar', 'fat', 'protein'],
  data() {
    return {
      loggedIn: false,
      isAdmin: false,
      deleteConfirm: false,
      editForm: false,
      new_name: this.food_name,
      new_brand: this.food_brand,
      new_score: this.food_score,
      new_energy: this.energy,
      new_carbohydrate: this.carbohydrate,
      new_sugar: this.sugar,
      new_fat: this.fat,
      new_protein: this.protein,
      score_options: ['A', 'B', 'C', 'D', 'E']
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
  },
  methods: {
    onDelete() {
      console.log(sessionStorage.getItem('userid'))
      let _this = this
      this.$axios.post('http://192.168.31.92:8000/api/delete', {
        uid: sessionStorage.getItem('userid'),
        food_id: _this.food_id
      }).then(function (response) {
        let res = response.data
        if(res.status !== 'Success') {
          _this.$q.notify({
            type: 'negative',
            message: 'Delete failed. ' + res.message
          })
        } else {
          _this.$router.push('/index')
        }
      }).catch(function (error) {
        console.log(error)
        _this.$q.notify({
          type: 'negative',
          message: 'Internal error.'
        })
      })
    },
    onEdit() {
      this.new_name = this.food_name
      this.new_brand = this.food_brand
      this.new_score = this.food_score
      this.new_energy = this.energy
      this.new_carbohydrate = this.carbohydrate
      this.new_sugar = this.sugar
      this.new_fat = this.fat
      this.new_protein = this.protein
      this.editForm = true
    },
    onSubmit() {
      let _this = this
      let newScore
      switch (this.new_score) {
        case 'A':
          newScore = 1
              break
        case 'B':
          newScore = 2
              break
        case 'C':
          newScore = 3
              break
        case 'D':
          newScore = 4
              break
        case 'E':
          newScore = 5
              break
        default:
          newScore = -1
              break
      }
      this.$axios.post('http://192.168.31.92:8000/api/update', {
        uid: sessionStorage.getItem('userid'),
        food_id: _this.food_id,
        score: newScore,
        carbohydrate: _this.new_carbohydrate,
        fat: _this.new_fat,
        sugar: _this.new_sugar,
        energy: _this.new_energy,
        protein: _this.new_protein
      }).then(function (response) {
        let res = response.data
        if(res.status !== 'Success') {
          _this.$q.notify({
            type: 'negative',
            message: 'Edit failed. ' + res.message
          })
        } else {
          _this.$router.push('/index')
        }
      }).catch(function (error) {
        console.log(error)
        _this.$q.notify({
          type: 'negative',
          message: 'Internal error.'
        })
      })
    }
  }
}
</script>

<style scoped>

</style>
