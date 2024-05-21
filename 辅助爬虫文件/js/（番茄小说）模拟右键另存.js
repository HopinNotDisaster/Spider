
// 写好之后复制到网站的控制台中！

let imgs = document.querySelectorAll("[id^=g]")
let gid = document.querySelector("#input-name")
// console.log(gid);
console.log(imgs);
imgs.forEach(function (item, index) {
    if (index >= 2 && index <= 101) {
        setTimeout(function () {
            // console.log(item)
            item.click();
            let img_name = gid.value;
            img_name = img_name.slice(3)
            console.log(img_name);
            let url = item.toDataURL("image/png");
            let a = document.createElement("a");
            a.href = url;
            a.download = `${img_name}.png`
            a.click();
        },500*index)
    }
})