// document.documentElement.setAttribute('data-bs-theme', 'dark');

function setTheme(theme) {
    document.documentElement.setAttribute('data-bs-theme', theme);
    localStorage.setItem('theme', theme);
}

function toggleThemeMenu() {
    const themeMenu = document.querySelector('#theme-menu');
    if (!themeMenu) return;

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        setTheme(savedTheme);
    }

    document.querySelectorAll('[data-bs-theme-value]').forEach(button => {
        button.addEventListener('click', () => {
            const theme = button.getAttribute('data-bs-theme-value');
            setTheme(theme);

            // Actualizar el aria-pressed
            document.querySelectorAll('[data-bs-theme-value]').forEach(b => {
                b.setAttribute('aria-pressed', 'false');
            });
            button.setAttribute('aria-pressed', 'true');
        });
    });
}

document.addEventListener('DOMContentLoaded', toggleThemeMenu);