const slider_span = document.querySelector(".breaking_news_slider_section");
let slider_text = document.querySelector(".breaking-news-slider-text");

const slider_span_width      = slider_span.clientWidth;
let slider_text_width      = slider_text.clientWidth;
var initial_position       = -slider_text_width;

var calSliderFunc;
console.log(slider_span_width);

// let arr = ["Hi, helli baby chocolate", "hello", "where are going?"];

let slider_Func = ()=>{

    slider_text.style.left = -slider_text_width + '0px';

        if(initial_position < slider_span_width){
            initial_position += 10;
            // slider_text.style.position = 'relative';
            slider_text.style.left = initial_position +"px";
            slider_text.style.transition = '0.5s';
            if(initial_position >= slider_span_width){
                initial_position = -slider_text_width;
                slider_text.style.left = -slider_text_width + 'px';
                slider_text.style.transition = '0s';
                slider_text.style.visibility = 'hidden';
            }else{
                slider_text.style.visibility = 'visible';
            }
        }

    }

    calSliderFunc = setInterval(slider_Func, 200);

    let stopAnimation = () =>{
        clearInterval(calSliderFunc);
    }

    let startAnimation = () =>{
        calSliderFunc = setInterval(slider_Func, 200);
    }
