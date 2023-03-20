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
  
      <div class="d-flex justify-center mx-auto">
        <v-container fluid>
            <v-row>
            <v-col cols="2"></v-col>
            <v-col cols="8">
            <span>请输入您需要拼接的片段数量 / </span>
            <span>Please input the segment number of assembly </span>
        <v-text-field
        label="Number input"
        :rules="rules"
        hide-details="auto"
        class="mb-10"
        ></v-text-field>
        <span>请输入您需要的重叠区域长度 / </span>
        <span>Please input the length of overlapped area </span>
        <v-text-field label="Length input"
        :rules="rules"
        hide-details="auto"
        class="mb-10"></v-text-field>
        <span>请按顺序输入每个片段的序列 / </span>
        <span>Please input the sequence of every segment in order</span>
        <v-textarea
          outlined
          class="my-10"
          name="input-7-4"
          label="Sequence input"
          value=""
        ></v-textarea>
        </v-col>
        <v-col cols="2"></v-col>
        </v-row>
    </v-container>
      </div>
  
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
    name: "SeqLineView",
  
    components: {},
    data: () => ({
        rules: [
          value => !!value || 'Required.'
        ],
        row: null,
      }),
    }
</script>