const WHATSAPP_NUMBER="989128692978";
function openWhatsApp(category){const text=encodeURIComponent(`Hello Keshmiri Rugs, I want to see more or purchase from the ${category||"Persian Rugs"} collection.`);window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${text}`,"_blank")}
document.addEventListener("click",e=>{const btn=e.target.closest("[data-wa]");if(btn)openWhatsApp(btn.dataset.category)});