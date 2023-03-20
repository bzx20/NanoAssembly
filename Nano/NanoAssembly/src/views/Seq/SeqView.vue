<template>
    <div>
      <v-card
      class="mx-auto mt-10"
      max-width="1400"
    >
      <v-img
        src="@/assets/Seq_Logo.png"
        height="200px"
      ></v-img>
  
      <v-card-title class="d-flex justify-center mx-auto text-h5">
        请选择您要使用的拼接方式
      </v-card-title>
      <v-card-subtitle class="d-flex justify-center mx-auto text-h6">
        Please choose the way of assembly
      </v-card-subtitle>
  
  
      <v-radio-group
        v-model="row"
        class="d-flex justify-center mx-auto"
        row
      >
      <div class="d-flex justify-center mx-auto">
        <v-radio
          label="环状拼接 / Circular Assembly"
          value="circ"
        ></v-radio>
        <v-radio
          label="线状拼接 / Linear Assembly"
          value="line"
        ></v-radio>
        </div>
      </v-radio-group>
  
      <v-card-actions>
        <div class="d-flex justify-center mx-auto my-3">
          <!-- Button clicked, change the page to seq if radio1 is selected, to str if radio2 is selected-->
        <v-btn
          color="green lighten-2"
          text
          @click="row === 'circ' ? $router.push('/seqcirc') : $router.push('/seqline')"
        >
          引物设计 / Primer Design
        </v-btn>
        <v-btn
          color="blue lighten-2"
          text
          @click="$router.push('/')"
        >
          退出 / Exit
        </v-btn>
        </div>

      </v-card-actions>
  
      
    </v-card>
    </div>
  </template>
  
  
  
  
  <script>
  export default {
    name: "SeqView",
  
    components: {},
    data: () => ({
        rules: [
          value => !!value || 'Required.',
          value => (value && value.length >= 3) || 'Min 3 characters',
        ],
        row: null,
      }),
    }
</script>