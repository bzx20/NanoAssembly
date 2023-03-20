<template>
  <div>
    <!-- 轮播图 -->
    <!-- <v-carousel
      cycle
      height="600"
      hide-delimiter-background
      show-arrows-on-hover
    >
      <v-carousel-item v-for="(slide, i) in slides" :key="i" :src="slide.src">
      </v-carousel-item>
    </v-carousel> -->

    <!-- 主体 -->
    <v-card
    class="mx-auto mt-10"
    max-width="1400"
  >
    <v-img
      src="@/assets/Nano_Logo.png"
      height="400px"
    ></v-img>

    <v-card-title class="d-flex justify-center mx-auto text-h5">
      请选择您要使用的工具
    </v-card-title>

    <v-card-subtitle class="d-flex justify-center mx-auto text-h6">
      Please choose the tool of assembly
    </v-card-subtitle>

    <v-radio-group
      v-model="row"
      class="d-flex justify-center mx-auto"
      row
    >
    <div class="d-flex justify-center mx-auto">
      <v-radio
        label="序列设计 / Sequence Design"
        value="seq"
      ></v-radio>
      <v-radio
        label="结构设计 / Structure Design"
        value="str"
      ></v-radio>
      </div>
    </v-radio-group>

    <v-card-actions>
      <div class="d-flex justify-center mx-auto my-3">
        <!-- Button clicked, change the page to seq if radio1 is selected, to str if radio2 is selected-->
      <v-btn
        color="green lighten-2"
        text
        @click="row === 'seq' ? $router.push('/seq') : $router.push('/')"
      >
        进入界面 / Enter
      </v-btn>
      <v-btn
        color="blue lighten-2"
        text
      >
        退出 / Exit
      </v-btn>
      </div>

      <!-- <v-spacer></v-spacer> -->
    </v-card-actions>

    
  </v-card>
  </div>
</template>




<script>
export default {
  name: "HomeView",

  components: {},
  data: () => ({
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
      row: null,
    }),
  //     overlay: false,
  //     slides: [
  //       {
  //         src: "https://cdn.vuetifyjs.com/images/cards/house.jpg",
  //       },
  //       {
  //         src: "https://cdn.vuetifyjs.com/images/cards/house.jpg",
  //       },
  //       {
  //         src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
  //       },
  //       {
  //         src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
  //       },
  //     ],
};
</script>
