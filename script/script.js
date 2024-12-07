const snowContainer = document.querySelector('.snow');

function createSnowflake() {
    const snowflake = document.createElement('div');
    snowflake.classList.add('snowflake');

    const size = Math.random() * 5 + 2; // Size between 2px and 7px
    snowflake.style.width = `${size}px`;
    snowflake.style.height = `${size}px`;

    snowflake.style.left = `${Math.random() * 100}vw`;
    
    const duration = Math.random() * 3 + 2; // Duration between 2s and 5s
    snowflake.style.animationDuration = `${duration}s`;

    snowContainer.appendChild(snowflake);

    setTimeout(() => {
        snowflake.remove();
    }, duration * 1000);
}

setInterval(createSnowflake, 300); // Create a snowflake every 300ms
