// Globals

var clickCount = {}
var showHidden = false;
// load click counts from local storage
var img_src_path = 'C:\\Dev\\html_apps\\home_page\\images\\'

var template = `<div class="container-item" data-url="{{URL}}">
    <button class="close-btn" onclick="toggleLinkActive('{{URL}}', event)">{{BUTTON}}</button>
    <div class="link-controls">
      <div class="link-controls-item" onclick=""></div>
    </div>
     <a target="_blank" href="{{URL}}" class="link" onclick="clicked('{{URL}}')"> 
         <img class="link-item" src="${img_src_path}{{IMG}}"/>{{ALT}}
         
     </a>
     <div class="link-name" title="Page visited {{CLICK_COUNT}} times!">{{NAME}}</div>
 </div>`

// Functions

function init() {
  clickCount = {};
  reset_clickCount();
  load_inactiveLinks();
  load_links();
  embed_spotify();
}

function load_links() {
  // update active flags based on inactiveLinks
  lst_general_links.forEach((link) => {
    link.clickCount = 0;
    if (clickCount[link.url]) {
      link.clickCount = clickCount[link.url];
    }
    // apply inactive state from storage
    if (inactiveLinks[link.url]) {
      link.isActive = false;
    }
  });

  // sort lst_general_links based on click count
  lst_general_links = lst_general_links.sort((a, b) => (a.clickCount < b.clickCount) ? 1 : -1);

  // General Links
  let el_general_links = document.getElementById('general-links')
  el_general_links.innerHTML = ''; // clear existing entries
  lst_general_links.forEach((link) => {
    link_template = template.replaceAll('{{URL}}', link.url)
    let link_name = link.name
    let link_img = link.img
    let link_alt = ''
    if (!link.img) {
      link_img = ''
      link_alt = link.url
    }
    link_template = link_template.replaceAll('{{NAME}}', link_name)
    link_template = link_template.replaceAll('{{IMG}}', link_img)
    link_template = link_template.replaceAll('{{ALT}}', link_alt)
    link_template = link_template.replaceAll('{{CLICK_COUNT}}', link.clickCount)
    // choose button label based on active state
    const btnLabel = link.isActive ? '\u00D7' : '+';
    link_template = link_template.replaceAll('{{BUTTON}}', btnLabel);

    let el_link = document.createElement('div')
    el_link.innerHTML = link_template
    let containerItem = el_link.firstChild
    containerItem.setAttribute('data-active', link.isActive)
    if (!link.isActive && !showHidden) {
      containerItem.style.display = 'none'
    }
    el_general_links.appendChild(containerItem)
  })

}

function toggleShowHidden(event) {
  showHidden = event.target.checked;
  const items = document.querySelectorAll('[data-active]');
  items.forEach((item) => {
    const isActive = item.getAttribute('data-active') === 'true';
    if (!isActive && !showHidden) {
      item.style.display = 'none';
    } else {
      item.style.display = '';
    }
  });
}

function embed_spotify() {
  // This is a high-level outline. Real implementation requires OAuth flow.
  fetch('https://api.spotify.com/v1/me/player/currently-playing', {
    headers: {
      'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    }
  })
    .then(response => response.json())
    .then(data => {
      const trackId = data.item.id;
      const embedUrl = `https://open.spotify.com/embed/track/${trackId}`;
      document.getElementById('spotify-player').src = embedUrl;
    });

}

// inactive links storage
var inactiveLinks = {};

function toggleLinkActive(url, event) {
  // decide based on current state
  if (inactiveLinks[url]) {
    reactivateLink(url, event);
  } else {
    deactivateLink(url, event);
  }
}

function reactivateLink(url, event) {
  event.stopPropagation();
  // remove from storage
  delete inactiveLinks[url];
  saveInactiveLinks();
  // update memory
  let linkObj = lst_general_links.find(l => l.url === url);
  if (linkObj) {
    linkObj.isActive = true;
  }
  // update DOM element
  let item = event.currentTarget.closest('.container-item');
  if (item) {
    item.setAttribute('data-active', 'true');
    // change button to ×
    let btn = item.querySelector('.close-btn');
    if (btn) btn.textContent = '\u00D7';
    // ensure it's visible
    item.style.display = '';
  }
}

function load_inactiveLinks() {
  try {
    inactiveLinks = JSON.parse(localStorage.getItem('inactiveLinksData')) || {};
  } catch (ex) {
    console.log('Exception While Loading Inactive Links: ', ex);
    inactiveLinks = {};
  }
}

function saveInactiveLinks() {
  try {
    localStorage.setItem('inactiveLinksData', JSON.stringify(inactiveLinks));
  } catch (ex) {
    console.log('Exception While Saving Inactive Links: ', ex);
  }
}

function deactivateLink(url, event) {
  event.stopPropagation();
  inactiveLinks[url] = true;
  saveInactiveLinks();
  // also update our in-memory link list if present
  let linkObj = lst_general_links.find(l => l.url === url);
  if (linkObj) {
    linkObj.isActive = false;
  }
  // update DOM element
  let item = event.currentTarget.closest('.container-item');
  if (item) {
    item.setAttribute('data-active', 'false');
    // change button to plus
    let btn = item.querySelector('.close-btn');
    if (btn) btn.textContent = '+';
    if (!showHidden) {
      item.style.display = 'none';
    }
  }
}

function authenticateSpotify() {
  // This function should handle the OAuth flow to get an access token
  const axios = require('axios');
  app.get('/callback', async (req, res) => {
    const code = req.query.code;
    const response = await axios.post('https://accounts.spotify.com/api/token', new URLSearchParams({
      grant_type: 'authorization_code',
      code,
      redirect_uri: 'http://localhost:3000/callback',
      client_id: 'YOUR_CLIENT_ID',
      client_secret: 'YOUR_CLIENT_SECRET'
    }), {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    });
    // response.data.access_token is your token
    res.json(response.data);
  });

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
    if (!clickCount) {
      clickCount = {};
    }
  }
  catch (ex) {
    console.log('Exception While Loading LocalStorage: ', ex);
  }
}

function saveClickCount() {
  try {
    localStorage.setItem('clickCountData', JSON.stringify(clickCount));
    reset_clickCount();
  }
  catch (ex) {
    console.log('Exception While Saving to LocalStorage: ', ex);
  }

}


init()
