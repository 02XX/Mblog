<script setup>


defineProps({
    articleBrief:{
        type: String,
        default: ""
    },
    articleTitle: {
        type: String,
        default: ""
    },
    articleId: Number,
})

</script>

<template>
    <el-card class="box-card">
        <template #header >
            <div class="card-header" >
                <span id="title">{{articleTitle}}</span>
            </div>
        </template>

        <div>{{ articleBrief }}</div>

        <div id="details">
        <router-link :to="'/article/' + articleId"><el-button class="button" text>阅读全文</el-button></router-link>
        </div>
    </el-card>
</template>

<style>
#title {
    font-size: 2.6rem;
    font-weight: bolder;
}


.card-header {
    display: flex;
    justify-content: center;
    align-items: center;
}

.text {
    font-size: 14px;
}

.item {
    margin-bottom: 18px;
}

.box-card {
    width: 100%;
    margin: 10px;
}

#details {
    display: flex;
    justify-content: center;
}
</style>
