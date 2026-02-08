const canvas = document.getElementById('iris-canvas');
const ctx = canvas.getContext('2d');
let chauffeurs = [];

function initGPS() {
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(updatePosition, null, { enableHighAccuracy: true });
        document.getElementById('data-status').innerText = "COLLECTE GPS ACTIVE";
    }
}

function updatePosition(pos) {
    const newCoord = {
        id: "CH-58",
        x: Math.random() * canvas.width, // Simulation mappage
        y: Math.random() * canvas.height,
        accuracy: pos.coords.accuracy
    };
    
    // Ajout si n'existe pas ou mise à jour
    chauffeurs = [newCoord]; // Pour l'exemple, on suit une unité
    render();
}

function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    chauffeurs.forEach(c => {
        // Point GPS
        ctx.fillStyle = "#00f2ff";
        ctx.beginPath();
        ctx.arc(c.x, c.y, 5, 0, Math.PI*2);
        ctx.fill();
        
        // Rayon de couplage (Magnétisme)
        ctx.strokeStyle = "rgba(255, 0, 255, 0.3)";
        ctx.beginPath();
        ctx.arc(c.x, c.y, 50, 0, Math.PI*2);
        ctx.stroke();
    });
}

// Mise à jour de l'horloge type SIEL
setInterval(() => {
    document.getElementById('clock').innerText = new Date().toLocaleTimeString();
}, 1000);
