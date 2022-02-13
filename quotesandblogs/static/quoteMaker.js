
    var opacityValue = document.getElementById("overLayRange")
    var colorValue = document.getElementById("colorSelector")
    var quoteInput = document.getElementById("quote_id")
    var authorInput = document.getElementById("author_id")
    var image = document.querySelector(".featuredImage")
    var overlay = document.querySelector(".overlay")
    var colorShow = document.getElementById("colorShow")
    var quote = document.querySelector(".quote__")
    var author = document.querySelector(".author__")

    var myFontQuote = document.getElementById("fonts_list_quote")
    var myFontAuthor = document.getElementById("fonts_list_author")

    var quoteStyleBar = document.querySelector('.edit_quote_')
    var authorStyleBar = document.querySelector('.edit_author_')

    var quoteFontSize = document.querySelector('.edit_quote_ input')
    var authorFontSize = document.querySelector('.edit_author_ input')

    var quoteFontSizeIncreaser = document.querySelector('.edit_quote_ .incFont')
    var quoteFontSizeDecreaser = document.querySelector('.edit_quote_ .decFont')

    var authorFontSizeIncreaser = document.querySelector('.edit_author_ .incFont')
    var authorFontSizeDecreaser = document.querySelector('.edit_author_ .decFont')

    var quoteAlignment = ""
    var authorAlignment = ""

    var quoteAlignmentLeft = document.querySelector('.edit_quote_ .alignLeft')
    var quoteAlignmentCenter = document.querySelector('.edit_quote_ .alignCenter')
    var quoteAlignmentRight = document.querySelector('.edit_quote_ .alignRight')

    var authorAlignmentLeft = document.querySelector('.edit_author_ .alignLeft')
    var authorAlignmentCenter = document.querySelector('.edit_author_ .alignCenter')
    var authorAlignmentRight = document.querySelector('.edit_author_ .alignRight')

    var root = document.querySelector(':root');

    var quoteColor = ''
    var quoteBold = ''
    var quoteItalic = ''

    var authorColor = ''
    var authorBold = ''
    var authorItalic = ''

    var quoteFontColor = document.querySelector('.edit_quote_ .fontColor')
    var quoteFontColorInput = document.querySelector('.edit_quote_ .selectColor')
    var quoteFontBold = document.querySelector('.edit_quote_ .fontBold')
    var quoteFontItalic = document.querySelector('.edit_quote_ .fontItalic')

    var authorFontColor = document.querySelector('.edit_author_ .fontColor')
    var authorFontColorInput = document.querySelector('.edit_author_ .selectColor')
    var authorFontBold = document.querySelector('.edit_author_ .fontBold')
    var authorFontItalic = document.querySelector('.edit_author_ .fontItalic')

    var imageInput =  document.querySelector('#file')

    var loadFile = function(event) {
	let imageMini = document.getElementById('output_');
	imageMini.src = URL.createObjectURL(event.target.files[0]);
    image.setAttribute('src', URL.createObjectURL(event.target.files[0]))
    // saveImageDataToStorage()
    };

    document.querySelector('.image__').addEventListener('click',()=>{
        imageInput.click()
    })

    quote.addEventListener('click',()=>{
        quoteStyleBar.classList.add('active_')
        quote.classList.add('selected_text_')
        author.classList.remove('selected_text_')
        authorStyleBar.classList.remove('active_')
    })

    author.addEventListener('click',()=>{
        quoteStyleBar.classList.remove('active_')
        quote.classList.remove('selected_text_')
        author.classList.add('selected_text_')
        authorStyleBar.classList.add('active_')
    })

    document.body.addEventListener('click', function(e) {
    if (
        !e.target.classList.contains('quote__')
        && !e.target.classList.contains('author__')
        && !e.target.classList.contains('fonts_list')
        && !e.target.classList.contains('incFont')
        && !e.target.classList.contains('decFont')
        && !e.target.classList.contains('showSize')
        && !e.target.classList.contains('alignLeft')
        && !e.target.classList.contains('alignCenter')
        && !e.target.classList.contains('fa-align-left')
        && !e.target.classList.contains('fa-align-center')
        && !e.target.classList.contains('fa-align-right')
        && !e.target.classList.contains('alignRight')
        && !e.target.classList.contains('fontColor')
        && !e.target.classList.contains('fontBold')
        && !e.target.classList.contains('fontItalic')
      ) {
        quote.classList.remove('selected_text_')
        author.classList.remove('selected_text_')
    }
    });

    //checks if already image and data in localStorage
    const imageData = JSON.parse(window.localStorage.getItem('imageData'))
    if(imageData){
        //quote
        quoteInput.value = imageData.quote
        quote.textContent = imageData.quote

        //author
        authorInput.value = imageData.author
        author.textContent=  imageData.author
        
        //background Image
        document.querySelector(".featuredImage").setAttribute('src',imageData.backgroundImage)

        //image for show mini
        // document.getElementById('output_').setAttribute('src',imageData.backgroundImage)

        //overlay color
        colorValue.value = imageData.overLayColor
        colorShow.textContent = imageData.overLayColor
        overlay.style.background = imageData.overLayColor

        //overlay color opacity
        opacityValue.value = imageData.overLayOpacity
        overlay.style.opacity = imageData.overLayOpacity/10
        
        //set font family
        quote.style.fontFamily = imageData.fontFamilyQuote,
        author.style.fontFamily = imageData.fontFamilyAuthor

        //set quote fontSize
        quoteFontSize.value = imageData.quoteFontSize
        quote.style.fontSize = imageData.quoteFontSize+'px'

        //set author fontSize
        authorFontSize.value = imageData.authorFontSize
        author.style.fontSize = imageData.authorFontSize+'px'

        //quote alignment
        quoteAlignment = imageData.quoteAlignment
        quote.style.textAlign = imageData.quoteAlignment
        if(quoteAlignment==="left"){
            quoteAlignmentLeft.classList.add('activeAlignment')
            quoteAlignmentCenter.classList.remove('activeAlignment')
            quoteAlignmentRight.classList.remove('activeAlignment')
        }
        else if(quoteAlignment==="center"){
            quoteAlignmentLeft.classList.remove('activeAlignment')
            quoteAlignmentCenter.classList.add('activeAlignment')
            quoteAlignmentRight.classList.remove('activeAlignment')
        }
        else{
            quoteAlignmentLeft.classList.remove('activeAlignment')
            quoteAlignmentCenter.classList.remove('activeAlignment')
            quoteAlignmentRight.classList.add('activeAlignment')
        }

        //quote alignment
        authorAlignment = imageData.authorAlignment
        author.style.textAlign = imageData.authorAlignment

        if(authorAlignment==="left"){
            authorAlignmentLeft.classList.add('activeAlignment')
            authorAlignmentCenter.classList.remove('activeAlignment')
            authorAlignmentRight.classList.remove('activeAlignment')
        }
        else if(authorAlignment==="center"){
            authorAlignmentLeft.classList.remove('activeAlignment')
            authorAlignmentCenter.classList.add('activeAlignment')
            authorAlignmentRight.classList.remove('activeAlignment')
        }
        else{
            authorAlignmentLeft.classList.remove('activeAlignment')
            authorAlignmentCenter.classList.remove('activeAlignment')
            authorAlignmentRight.classList.add('activeAlignment')
        }

        //quote color
        quoteFontColorInput.value = imageData.quoteFontColor
        quote.style.color = imageData.quoteFontColor
        root.style.setProperty('--quoteColor', imageData.quoteFontColor)

         //author color
        authorFontColorInput.value = imageData.authorFontColor
        author.style.color = imageData.authorFontColor
        root.style.setProperty('--authorColor', imageData.authorFontColor)


        //quote bold
        quoteBold = imageData.quoteFontBold
        if(quoteBold==='800'){
            quote.style.fontWeight = quoteBold
            quoteFontBold.classList.add('activeAlignment')
        }
        else{
            quote.style.fontWeight = quoteBold
            quoteFontBold.classList.remove('activeAlignment')
        }

        //quote italic
        quoteItalic = imageData.quoteFontItalic
        if(quoteItalic==='italic'){
            quote.style.fontStyle = quoteItalic
            quoteFontItalic.classList.add('activeAlignment')
        }
        else{
            quote.style.fontStyle = quoteItalic
            quoteFontItalic.classList.remove('activeAlignment')
        }


        //author bold
        authorBold = imageData.authorFontBold
        if(authorBold==='800'){
            author.style.fontWeight = authorBold
            authorFontBold.classList.add('activeAlignment')
        }
        else{
            author.style.fontWeight = authorBold
            authorFontBold.classList.remove('activeAlignment')
        }

        //author italic
        authorItalic = imageData.authorFontItalic
        if(authorItalic==='italic'){
            author.style.fontStyle = authorItalic
            authorFontItalic.classList.add('activeAlignment')
        }
        else{
            author.style.fontStyle = authorItalic
            authorFontItalic.classList.remove('activeAlignment')
        }
        

    }

    const saveImageDataToStorage = () =>{
        const imageData = {
        quote :  quoteInput.value,
        author :  authorInput.value,
        backgroundImage : document.querySelector(".featuredImage").getAttribute('src'),
        overLayColor :  colorValue.value,
        overLayOpacity :  opacityValue.value,
        fontFamilyQuote : myFontQuote.value,
        fontFamilyAuthor : myFontAuthor.value,
        quoteFontSize : quoteFontSize.value,
        authorFontSize : authorFontSize.value,
        quoteAlignment : quoteAlignment,
        authorAlignment : authorAlignment,
        quoteFontColor : quoteFontColorInput.value,
        authorFontColor : authorFontColorInput.value,
        quoteFontBold : quoteBold,
        authorFontBold : authorBold,
        quoteFontItalic : quoteItalic,
        authorFontItalic : authorItalic
        }
        window.localStorage.setItem('imageData',JSON.stringify(imageData))
    }


    const downloadImage_ = ()=>{
        html2canvas(document.querySelector("#capture")).then(canvas => {
        var a = document.createElement('a');
        a.href = canvas.toDataURL("image/jpeg").replace("image/jpeg", "image/octet-stream");
        a.download = 'quote.jpg';
        a.click();
        });  
    } 
    
    //download image
    document.querySelector(".secondbtn_").addEventListener('click',downloadImage_)

    //download image
    try{    document.querySelector(".download_").addEventListener('click',downloadImage_)}
    catch(e){}

    


    // *************************font family options and set in select field******************************
    const fontOptions = [
        'Amita',
        'Anton',
        'Bebas Neue',
        'Berkshire Swash',
        'Bubblegum Sans',
        'Bungee',
        'Bungee Inline',
        'Bungee Shade',
        'Dancing Script',
        'Fredericka the Great',
        'Just Me Again Down Here',
        'Kalam',
        'Lobster Two',
        'Lora',
        'Metal Mania',
        'Monofett',
        'Montserrat',
        'Oswald',
        'Pacifico',
        'Permanent Marker',
        'Press Start 2P',
        'PT Sans',
        'Roboto',
        'Roboto Slab',
        'Rock Salt',
        'Rubik Mono One',
        'Sarpanch',
        'Satisfy',
        'Shadows Into Light',
        'Tourney'
    ]

    fontOptions.forEach((x)=>{
        const option = document.createElement('option');
        option.setAttribute('value',x)
        option.textContent = x
        option.style.fontFamily = x
        myFontQuote.appendChild(option)
        myFontQuote.value = imageData.fontFamilyQuote ? imageData.fontFamilyQuote : 'Kalam'
    })

    fontOptions.forEach((x)=>{
        const option = document.createElement('option');
        option.setAttribute('value',x)
        option.textContent = x
        option.style.fontFamily = x
        myFontAuthor.appendChild(option)
        myFontAuthor.value = imageData.fontFamilyAuthor ? imageData.fontFamilyAuthor : 'Kalam'
    })

    // *************************END font family options and set in select field******************************

    colorValue.addEventListener('input',(e)=>{
        overlay.style.background=e.target.value
        colorShow.textContent=e.target.value
        saveImageDataToStorage()
    })

    opacityValue.addEventListener("change",(e)=>{
        overlay.style.opacity=e.target.value/10
        saveImageDataToStorage()
    })

    quoteInput.addEventListener("keyup",(e)=>{
        quote.textContent=e.target.value
        saveImageDataToStorage()
    })

    authorInput.addEventListener("keyup",(e)=>{
        author.textContent=  e.target.value
        saveImageDataToStorage()
    })

    myFontQuote.addEventListener('change',(e)=>{
     quote.style.fontFamily = e.target.value
     saveImageDataToStorage()
    })

    myFontAuthor.addEventListener('change',(e)=>{
     author.style.fontFamily = e.target.value
     saveImageDataToStorage()
    })

    quoteFontSize.addEventListener('keyup',(e)=>{
        quote.style.fontSize = e.target.value+'px'
        saveImageDataToStorage()
    })

    quoteFontSize.addEventListener('keyup',(e)=>{
        if(e.key=== "ArrowUp"){
            quoteFontSize.value++
            quote.style.fontSize = e.target.value+'px'
            saveImageDataToStorage()
        }
        if(e.key==="ArrowDown"){
            quoteFontSize.value--
            quote.style.fontSize = e.target.value+'px'
            saveImageDataToStorage()
        }
    })

    authorFontSize.addEventListener('keyup',(e)=>{
        author.style.fontSize = e.target.value+'px'
        saveImageDataToStorage()
    })

    authorFontSize.addEventListener('keyup',(e)=>{
        if(e.key=== "ArrowUp"){
            authorFontSize.value++
            author.style.fontSize = e.target.value+'px'
            saveImageDataToStorage()
        }
        if(e.key==="ArrowDown"){
            authorFontSize.value--
            author.style.fontSize = e.target.value+'px'
            saveImageDataToStorage()
        }
    })

    quoteFontSizeIncreaser.addEventListener('click',()=>{
        quoteFontSize.value++
        quote.style.fontSize =  quoteFontSize.value +'px'
        saveImageDataToStorage()
    })

    quoteFontSizeDecreaser.addEventListener('click',()=>{
        quoteFontSize.value--
        quote.style.fontSize =  quoteFontSize.value +'px'
        saveImageDataToStorage()
    })

    authorFontSizeIncreaser.addEventListener('click',()=>{
        authorFontSize.value++
        author.style.fontSize =  authorFontSize.value +'px'
        saveImageDataToStorage()
    })

    authorFontSizeDecreaser.addEventListener('click',()=>{
        authorFontSize.value--
        author.style.fontSize =  authorFontSize.value +'px'
        saveImageDataToStorage()
    })

    quoteAlignmentLeft.addEventListener('click',()=>{
        quoteAlignment = "left"
        quote.style.textAlign = quoteAlignment
        saveImageDataToStorage()

        quoteAlignmentLeft.classList.add('activeAlignment')
        quoteAlignmentCenter.classList.remove('activeAlignment')
        quoteAlignmentRight.classList.remove('activeAlignment')
    })

    quoteAlignmentCenter.addEventListener('click',()=>{
        quoteAlignment = "center"
        quote.style.textAlign = quoteAlignment
        saveImageDataToStorage()

        quoteAlignmentLeft.classList.remove('activeAlignment')
        quoteAlignmentCenter.classList.add('activeAlignment')
        quoteAlignmentRight.classList.remove('activeAlignment')
    })

    quoteAlignmentRight.addEventListener('click',()=>{
        quoteAlignment = "right"
        quote.style.textAlign = quoteAlignment
        saveImageDataToStorage()

        quoteAlignmentLeft.classList.remove('activeAlignment')
        quoteAlignmentCenter.classList.remove('activeAlignment')
        quoteAlignmentRight.classList.add('activeAlignment')
    })

    authorAlignmentLeft.addEventListener('click',()=>{
        authorAlignment = "left"
        author.style.textAlign = authorAlignment
        saveImageDataToStorage()

        authorAlignmentLeft.classList.add('activeAlignment')
        authorAlignmentCenter.classList.remove('activeAlignment')
        authorAlignmentRight.classList.remove('activeAlignment')
    })

    authorAlignmentCenter.addEventListener('click',()=>{
        authorAlignment = "center"
        author.style.textAlign = authorAlignment
        saveImageDataToStorage()

        authorAlignmentLeft.classList.remove('activeAlignment')
        authorAlignmentCenter.classList.add('activeAlignment')
        authorAlignmentRight.classList.remove('activeAlignment')
    })

    authorAlignmentRight.addEventListener('click',()=>{
        authorAlignment = "right"
        author.style.textAlign = authorAlignment
        saveImageDataToStorage()

        authorAlignmentLeft.classList.remove('activeAlignment')
        authorAlignmentCenter.classList.remove('activeAlignment')
        authorAlignmentRight.classList.add('activeAlignment')
    })

    quoteFontColor.addEventListener('click',()=>{
        quoteFontColorInput.click()
    })

    quoteFontColorInput.addEventListener('input',(e)=>{
        quote.style.color = e.target.value
        quoteFontColorInput.value = e.target.value
        root.style.setProperty('--quoteColor', e.target.value)
        saveImageDataToStorage()
    })

    quoteFontBold.addEventListener('click',()=>{
        if(quoteBold==='800'){
            quoteBold = '400'
            quote.style.fontWeight = quoteBold
            quoteFontBold.classList.remove('activeAlignment')
            saveImageDataToStorage()
        }
        else{
            quoteBold = '800'
            quote.style.fontWeight = quoteBold
            quoteFontBold.classList.add('activeAlignment')
            saveImageDataToStorage()
        }
       
    })

    quoteFontItalic.addEventListener('click',()=>{
        if(quoteItalic==='italic'){
            quoteItalic = 'normal'
            quote.style.fontStyle = quoteItalic
            quoteFontItalic.classList.remove('activeAlignment')
            saveImageDataToStorage()
        }
        else{
            quoteItalic = 'italic'
            quote.style.fontStyle = quoteItalic
            quoteFontItalic.classList.add('activeAlignment')
            saveImageDataToStorage()
        }
       
    })

    authorFontColor.addEventListener('click',()=>{
        authorFontColorInput.click()
    })

    authorFontColorInput.addEventListener('input',(e)=>{
        author.style.color = e.target.value
        authorFontColorInput.value = e.target.value
        root.style.setProperty('--authorColor', e.target.value)
        saveImageDataToStorage()
    })

    authorFontBold.addEventListener('click',()=>{
        if(authorBold==='800'){
            authorBold = '400'
            author.style.fontWeight = authorBold
            authorFontBold.classList.remove('activeAlignment')
            saveImageDataToStorage()
        }
        else{
            authorBold = '800'
            author.style.fontWeight = authorBold
            authorFontBold.classList.add('activeAlignment')
            saveImageDataToStorage()
        }
       
    })

    authorFontItalic.addEventListener('click',()=>{
        if(authorItalic==='italic'){
            authorItalic = 'normal'
            author.style.fontStyle = authorItalic
            authorFontItalic.classList.remove('activeAlignment')
            saveImageDataToStorage()
        }
        else{
            authorItalic = 'italic'
            author.style.fontStyle = authorItalic
            authorFontItalic.classList.add('activeAlignment')
            saveImageDataToStorage()
        }
       
    })
