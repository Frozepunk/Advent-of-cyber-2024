const snowContainer = document.querySelector('.snow');

function createSnowflake() {
    const snowflake = document.createElement('div');
    snowflake.classList.add('snowflake');

    // Randomize the size of the snowflake
    const size = Math.random() * 5 + 2; // Size between 2px and 7px
    snowflake.style.width = `${size}px`;
    snowflake.style.height = `${size}px`;

    // Randomize the position
    snowflake.style.left = `${Math.random() * 100}vw`;
    
    // Randomize the animation duration
    const duration = Math.random() * 3 + 2; // Duration between 2s and 5s
    snowflake.style.animationDuration = `${duration}s`;

    // Append the snowflake to the container
    snowContainer.appendChild(snowflake);

    // Remove the snowflake after it falls
    setTimeout(() => {
        snowflake.remove();
    }, duration * 1000);
}

// Create snowflakes at intervals
setInterval(createSnowflake, 300); // Create a snowflake every 300ms
