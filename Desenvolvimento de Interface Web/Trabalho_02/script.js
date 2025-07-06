/**
 * MOMENTOS ETERNOS - JavaScript Simplificado
 * Funcionalidades essenciais com código limpo e moderno
 */

// ===== CONFIGURAÇÃO =====
const CONFIG = {
  scrollOffset: 50,
  animationDelay: 5000
};

// ===== INICIALIZAÇÃO =====
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initNavigation();
  initForm();
  initTestimonials();
  setMinDate();
});

// ===== TEMA =====
function initTheme() {
  const toggle = document.querySelector('.theme-toggle');
  const icon = document.querySelector('.theme-icon');
  
  // Verifica preferência salva ou do sistema
  const savedTheme = localStorage.getItem('theme');
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  const currentTheme = savedTheme || systemTheme;
  
  if (currentTheme === 'dark') {
    document.documentElement.classList.add('dark');
    icon.textContent = '☀️';
  }
  
  toggle.addEventListener('click', () => {
    const isDark = document.documentElement.classList.toggle('dark');
    icon.textContent = isDark ? '☀️' : '🌙';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  });
}

// ===== NAVEGAÇÃO =====
function initNavigation() {
  const header = document.querySelector('.header');
  const links = document.querySelectorAll('.nav__link');
  
  // Header scroll effect
  let lastScroll = 0;
  window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;
    
    if (currentScroll > CONFIG.scrollOffset) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    
    lastScroll = currentScroll;
  });
  
  // Navegação suave e link ativo
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      
      if (href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        
        if (target) {
          const offset = target.offsetTop - 70;
          window.scrollTo({
            top: offset,
            behavior: 'smooth'
          });
        }
      }
    });
  });
  
  // Atualiza link ativo baseado no scroll
  const sections = document.querySelectorAll('section[id]');
  
  function updateActiveLink() {
    const scrollY = window.scrollY + 100;
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');
      
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        links.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }
  
  window.addEventListener('scroll', updateActiveLink);
  updateActiveLink();
}

// ===== FORMULÁRIO =====
function initForm() {
  const form = document.getElementById('contact-form');
  const successMessage = form.querySelector('.form-success');
  
  // Formatação automática do telefone
  const phoneInput = document.getElementById('telefone');
  phoneInput.addEventListener('input', (e) => {
    let value = e.target.value.replace(/\D/g, '');
    
    if (value.length > 10) {
      value = value.replace(/^(\d{2})(\d{5})(\d{4}).*/, '($1) $2-$3');
    } else if (value.length > 5) {
      value = value.replace(/^(\d{2})(\d{4})(\d{0,4}).*/, '($1) $2-$3');
    } else if (value.length > 2) {
      value = value.replace(/^(\d{2})(\d{0,5})/, '($1) $2');
    }
    
    e.target.value = value;
  });
  
  // Envio do formulário
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Simula envio (substitua por sua lógica real)
    const button = form.querySelector('button[type="submit"]');
    const originalText = button.textContent;
    
    button.textContent = 'Enviando...';
    button.disabled = true;
    
    // Simula delay de envio
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Mostra mensagem de sucesso
    successMessage.hidden = false;
    form.reset();
    
    button.textContent = originalText;
    button.disabled = false;
    
    // Esconde mensagem após 5 segundos
    setTimeout(() => {
      successMessage.hidden = true;
    }, 5000);
  });
}

// ===== DEPOIMENTOS =====
function initTestimonials() {
  const inputs = document.querySelectorAll('.testimonial-input');
  let currentIndex = 0;
  
  // Auto-play
  function nextTestimonial() {
    currentIndex = (currentIndex + 1) % inputs.length;
    inputs[currentIndex].checked = true;
  }
  
  let interval = setInterval(nextTestimonial, CONFIG.animationDelay);
  
  // Pausa ao interagir
  const testimonials = document.querySelector('.testimonials');
  
  testimonials.addEventListener('mouseenter', () => {
    clearInterval(interval);
  });
  
  testimonials.addEventListener('mouseleave', () => {
    interval = setInterval(nextTestimonial, CONFIG.animationDelay);
  });
  
  // Pausa ao selecionar manualmente
  inputs.forEach((input, index) => {
    input.addEventListener('change', () => {
      currentIndex = index;
      clearInterval(interval);
      interval = setInterval(nextTestimonial, CONFIG.animationDelay);
    });
  });
}

// ===== UTILITÁRIOS =====
function setMinDate() {
  const dateInput = document.getElementById('data');
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.setAttribute('min', today);
  }
}

// ===== MELHORIAS DE PERFORMANCE =====
// Lazy loading de imagens já está no HTML
// Intersection Observer para animações sob demanda
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.animationPlayState = 'running';
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Observa elementos animados
document.addEventListener('DOMContentLoaded', () => {
  const animatedElements = document.querySelectorAll('.benefit-card, .portfolio-item');
  animatedElements.forEach(el => {
    el.style.animationPlayState = 'paused';
    observer.observe(el);
  });
});