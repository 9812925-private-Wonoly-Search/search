const WONOLY_PACKAGES_API = "https://packages-chi.vercel.app/";
function loadInstantAnswers(cb) {
    const params = new Proxy(new URLSearchParams(window.location.search), {
        get: (searchParams, prop) => searchParams.get(prop),
    });

    const search_param = params.q;

    fetch(`${WONOLY_PACKAGES_API}?q=${encodeURIComponent(search_param)}`).then((res) => res.json()).then((json) => {
        if (JSON.stringify(json) != "{}") {
            document.getElementById("navigation__bar").classList.add("border-b");
            document.getElementById("navigation__bar").classList.add("border-black");
            document.getElementById("navigation__bar").classList.add("py-5");
    
            document.getElementById("instant__answer__wrapper").classList.add("py-5");
    
            let info   = json.info  ;
            let render = json.render;
    
            document.getElementById("instant__answer__wrapper").insertAdjacentHTML('beforeend', `
                <div class="ml-40 w-690 shadow-info_box text-info_box_cl border border-info_box_bg bg-info_box_bg p-5 rounded">
                    ${render.html}
                </div>
                <style>
                    ${render.css}
                </style>
    
                <!-- instant answer info -->
                <div>
                    <div id="instant__answer__info__open" class="ml-5 w-6 h-6 rounded relative shadow-info_box text-info_box_cl border border-info_box_bg bg-info_box_bg cursor-pointer border border-black flex items-center justify-center">
                        <svg class="w-full h-full" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </div>
                    <div id="instant__answer__info__close" class="hidden ml-5 w-6 h-6 rounded relative shadow-info_box text-info_box_cl border border-info_box_bg bg-info_box_bg cursor-pointer border border-black flex items-center justify-center">
                        <svg class="w-full h-full" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"></path></svg>
                    </div>
                    <div id="instant__answer__info__dialog" class="hidden ml-5 mt-2 w-80 shadow-info_box text-info_box_cl border border-info_box_bg bg-info_box_bg p-5 rounded">
                        <h2 style="font-size: 21px;">${info.title}</h2>
                        <p>${info.description}</p>
                        <p style="font-size: 15px;" class="mt-2">Made by <b>${info.author}</b>. Version <b>${info.version}</b></p>
                    </div>
                </div>
            `)
    
            // Create a script tag separately so that it executes
            var script = document.createElement('script');
            script.textContent = render.js;
            document.body.appendChild(script);
    
            cb();
        }
    }).catch(e => console.log(e))
}

window.addEventListener("load", () => {
    loadInstantAnswers(() => {
        let open_button = document.getElementById("instant__answer__info__open");
        let close_button = document.getElementById("instant__answer__info__close");
        let answer_dialog = document.getElementById("instant__answer__info__dialog");

        open_button.addEventListener("click", () => {
            open_button.classList.add("hidden");
            close_button.classList.remove("hidden");
            answer_dialog.classList.remove("hidden");
        })

        close_button.addEventListener("click", () => {
            close_button.classList.add("hidden");
            answer_dialog.classList.add("hidden");
            open_button.classList.remove("hidden");
        })
    })
})