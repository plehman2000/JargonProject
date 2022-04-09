<template>
    <body>
        <form action="/">
            <input type="submit" value="Submit Another Pdf" />
        </form>
        <p>{{this.pdftext}}</p>
    </body>    
</template>


<script>
export default {
  name: 'TextDisplay',
  props: ['pdftext']
}
</script>



