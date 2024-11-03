// Globals

var clickCount = {}
// load click counts from local storage
var img_src_path = 'C:\\Dev\\html_apps\\home_page\\images\\'

var template = `<div class="container-item">
     <a target="_blank" href="{{URL}}" class="link" onclick="clicked('{{URL}}')"> 
         <img class="link-item" src="${img_src_path}{{IMG}}"/>{{ALT}}
         
     </a>
     <div class="link-name">{{NAME}}</div>
 </div>`

// Functions

function init() {
  reset_clickCount();
  load_links()
}

function load_links() {
  // sort lst_general_links based on click count
  lst_general_links.forEach((link) => {
    link.clickCount = 0;
    if(clickCount[link.url]) {
      link.clickCount = clickCount[link.url];
    }
  });
  lst_general_links = lst_general_links.sort((a, b) => (a.clickCount < b.clickCount) ? 1 : -1);
  

  // General Links
  let el_general_links = document.getElementById('general-links')
  lst_general_links.forEach((link) => {
    link_template = template.replaceAll('{{URL}}', link.url)
    if (link.img != undefined) {
      link_template = link_template.replaceAll('{{NAME}}', link.name)
      link_template = link_template.replaceAll('{{IMG}}', link.img)
      link_template = link_template.replaceAll('{{ALT}}', '')
    }
    else {
      link_template = link_template.replaceAll('{{NAME}}', link.name)
      link_template = link_template.replaceAll('{{IMG}}', '')
      link_template = link_template.replaceAll('{{ALT}}', link.url)
    }
    let el_link = document.createElement('div')
    el_link.innerHTML = link_template
    el_general_links.appendChild(el_link.firstChild)
  })

}

function clicked(url) {
  console.log('clicked', url);

  reset_clickCount();
  if (Object.keys(clickCount).indexOf(url) >= 0) {
    clickCount[url] += 1
  }
  else {
    clickCount[url] = 1
  }
  saveClickCount();
}

function reset_clickCount() {
  try {
    clickCount = JSON.parse(localStorage.getItem('clickCountData'));
  }
  catch(ex) {
    console.log('Exception While Loading LocalStorage: ', ex);
  }
}

function saveClickCount() {
  try {
    localStorage.setItem('clickCountData', JSON.stringify(clickCount));
    reset_clickCount();
  }
  catch(ex) {
    console.log('Exception While Saving to LocalStorage: ', ex);
  }
  
}


init()
