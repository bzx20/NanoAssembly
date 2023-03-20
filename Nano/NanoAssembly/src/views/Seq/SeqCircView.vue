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
        v-model = "segNum"
        ></v-text-field>
        <span>请输入您需要的重叠区域长度 / </span>
        <span>Please input the length of overlapped area </span>
        <v-text-field label="Length input"
        :rules="rules"
        v-model="overlapLen"
        hide-details="auto"
        class="mb-10"></v-text-field>
        <span>请输入您需要的标记数量 / </span>
            <span>Please input the number of chemical modification </span>
        <v-text-field
        label="Number input"
        :rules="rules"
        hide-details="auto"
        class="mb-10"
        v-model = "num_cm"
        ></v-text-field>
        <span>请按顺序输入每个片段的序列 / </span>
        <span>Please input the sequence of every segment in order</span>
        <v-textarea
          outlined
          class="my-10"
          label="Sequence input"
          v-model="eachSeq"
          auto-grow
        ></v-textarea>
        </v-col>
        <v-col cols="2"></v-col>
        </v-row>
    </v-container>
      </div>
  
      <v-card-actions>
        <div class="d-flex justify-center mx-auto my-1">
          <!-- Button clicked, change the page to seq if radio1 is selected, to str if radio2 is selected-->
        <v-btn
          color="green lighten-2"
          text
          @click="calSeq()"
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
      <v-container fluid class="my-10">
        <v-row>
        <v-col cols="2"></v-col>
            <v-col cols="8">
              <span>这是引物设计的输出结果 / </span>
            <span>This is the output of the primer design </span>
      <v-textarea
          label="Output-Result"
          v-model = "output"
          class="my-10"
          auto-grow
          outlined
        ></v-textarea>
        </v-col>
        <v-col cols="2"></v-col>
        </v-row>
      
      
      <v-card-actions>
        <div class="d-flex justify-center mx-auto mb-10">
          <!-- Button clicked, change the page to seq if radio1 is selected, to str if radio2 is selected-->
        <v-btn
          color="green lighten-2"
          text
          @click="download()"
        >
          导出文件 / Download
        </v-btn>
        </div>

      </v-card-actions>
    </v-container>
    </v-card>
    </div>
  </template>
  
  <script>
  // import { onBeforeMount } from 'vue';
  // import { loadPyodide } from 'pyodide';
  // let pyodide;
  // import axios from 'axios';
  // import XLSX from 'xlsx'
  export default {
    name: "SeqCircView",
  
    components: {},
    data: () => ({
        rules: [
          value => !!value || 'Required.'
        ],
        row: null,
        output: "",
        segNum: "",
        overlapLen: "",
        eachSeq: "",
        num_cm: "",
      }),

    //第一步：load pyodide.js
    // onBeforeMount(() => {
    //   //加载pyodide.js
    //   let script = document.createElement('script');
    //   script.type = 'text/javascript';
    //   script.src = '/public/pyodide-core-0.22.1/pyodide.js';
    //   console.log("scriptUrl: " + script.src);
    //   document.body.appendChild(script);
    // }),

    methods: {
      calSeq(){
        // change seqNum, overlapLen to int
        this.segNum = parseInt(this.segNum);
        this.overlapLen = parseInt(this.overlapLen);
        this.num_cm = parseInt(this.num_cm);
        // fetch api
        let data = {"seqNum": this.segNum, "overLapLen": this.overlapLen, "eachSeq": this.eachSeq, "num_cm": this.num_cm}
                return fetch("/api/calseq",{
                    method: 'POST',
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then(res => {
                    console.log(res);
                    this.output = res["data"];
                    // 强制刷新页面
                    this.$forceUpdate();
                })
      },
      // getFileNameFromHeader(header) {
      //   if (!header) return null;

      //   var match = header.match(/filename=(?:"([^"]+)"|([^;]+))/i);
      //   if (match) return match[1] || match[2];

      //   var encodedMatch = header.match(/filename\*=UTF-8''([^;]+)/i);
      //   if (encodedMatch) return decodeURIComponent(encodedMatch[1]);

      //   return null;
      // },
      download(){
        let data = {"num_cm": this.num_cm}
            return fetch("/api/download",{
                    method: 'POST',
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then(res => {
                  // var fileName = getFileNameFromHeader(res.headers.get('content-disposition'));
                  var fileName = "data.csv";
                  // var keys = Object.keys(res[0]);
                  // var csv = keys.join(",") + "\n";
                  // for (var i = 0; i < res.length; i++) {
                  //   var values = Object.values(res[i]);
                  //   csv += values.join(",") + "\n";
                  // }
                  // get file content as text
                  // return res.text().then(text => {
                  // download csv file
                  var blob = new Blob([res], {type: "text/csv"}); // text/csv
                  var link = document.createElement("a");
                  link.href = window.URL.createObjectURL(blob);
                  link.download = fileName;
                  link.click();
                  // refresh page
                  // window.location.reload();
                  // });
                })
                .catch(err => console.error(err));
                    // console.log(res);
                    // // download the csv attachment
                    // var blob = new Blob([res.data], {type: "text/csv"});
                    // var link = document.createElement("a");
                    // link.href = window.URL.createObjectURL(blob);
                    // link.download = "data.csv";
                    // link.click();
                    // // 强制刷新页面
                    // this.$forceUpdate();
                // })
        // 前端 var wb = XLSX.utils.book_new(); // 创建一个工作簿 var ws = XLSX.utils.aoa_to_sheet(data); // 将数据转换为工作表 XLSX.utils.book_append_sheet(wb, ws, “Sheet1”); // 将工作表添加到工作簿 var wbout = XLSX.write(wb, {bookType:‘csv’, type:‘array’}); // 将工作簿写入csv格式的二进制数组 var blob = new Blob([wbout], {type:“text/csv”}); // 创建一个blob对象 var url = window.URL.createObjectURL(blob); // 生成一个临时的url window.open(url); // 打开新窗口下载文件
      }
    
    // 第二步：load自己写的python wheel
    // async installPyWheel(){ 
    //   pyodide = await loadPyodide();
    //   await pyodide.loadPackage("micropip");
    //   const micropip = pyodide.pyimport("micropip");
    //   await micropip.install('/test-1.0.0-py3-none-any.whl'); //test.whl为自己写的python程序编译成的whl文件
    // },
    
    // clickDesignBtn(){
    //   console.log(pyodide);
    //   if(pyodide == undefined)
    //   {
    //     this.installPyWheel(); 
    //   }
    //   this.calSeq(this.segNum, this.overlapLen, this.eachSeq);
    // },
    
    // // 第三步：使用python wheel中的方法
    // calSeq(segNum, overlapLen, eachSeq){
    //   const main = pyodide.pyimport("test"); //"main"为python程序中的文件名
    //   console.log(main);
    //   this.output = main.Cal(segNum, overlapLen, eachSeq); 
    // }
  }
};
</script>