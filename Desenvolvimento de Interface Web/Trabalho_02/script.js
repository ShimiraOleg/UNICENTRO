/**
 * MOMENTOS ETERNOS - JavaScript Corrigido
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
  initAnimations();
});

// ===== TEMA =====
function initTheme() {
  const toggle = document.querySelector('.theme-toggle');
  const icon = document.querySelector('.theme-icon');
  
  if (!toggle || !icon) return;
  
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
  
  if (!header) return;
  
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
      
      if (href && href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        
        if (target) {
          const headerHeight = header.offsetHeight || 70;
          const offset = target.offsetTop - headerHeight;
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
  if (!form) return;
  
  const successMessage = form.querySelector('.form-success');
  
  // Formatação automática do telefone
  const phoneInput = document.getElementById('telefone');
  if (phoneInput) {
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
  }
  
  // Validação em tempo real
  const inputs = form.querySelectorAll('input[required], textarea[required]');
  inputs.forEach(input => {
    input.addEventListener('blur', validateField);
    input.addEventListener('input', clearError);
  });
  
  function validateField(e) {
    const field = e.target;
    const errorMessage = field.parentNode.querySelector('.error-message');
    
    if (!field.checkValidity() && field.value.trim() !== '') {
      field.classList.add('error');
      if (errorMessage) {
        errorMessage.style.display = 'block';
      }
    } else {
      field.classList.remove('error');
      if (errorMessage) {
        errorMessage.style.display = 'none';
      }
    }
  }
  
  function clearError(e) {
    const field = e.target;
    const errorMessage = field.parentNode.querySelector('.error-message');
    
    if (field.checkValidity()) {
      field.classList.remove('error');
      if (errorMessage) {
        errorMessage.style.display = 'none';
      }
    }
  }
  
  // Envio do formulário
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Valida todos os campos obrigatórios
    let isValid = true;
    inputs.forEach(input => {
      if (!input.checkValidity()) {
        isValid = false;
        input.classList.add('error');
        const errorMessage = input.parentNode.querySelector('.error-message');
        if (errorMessage) {
          errorMessage.style.display = 'block';
        }
      }
    });
    
    if (!isValid) return;
    
    // Simula envio (substitua por sua lógica real)
    const button = form.querySelector('button[type="submit"]');
    const originalText = button.textContent;
    
    button.textContent = 'Enviando...';
    button.disabled = true;
    
    try {
      // Simula delay de envio
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Mostra mensagem de sucesso
      if (successMessage) {
        successMessage.hidden = false;
        successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      
      form.reset();
      
      // Esconde mensagem após 5 segundos
      setTimeout(() => {
        if (successMessage) {
          successMessage.hidden = true;
        }
      }, 5000);
      
    } catch (error) {
      console.error('Erro ao enviar formulário:', error);
      alert('Erro ao enviar formulário. Tente novamente.');
    } finally {
      button.textContent = originalText;
      button.disabled = false;
    }
  });
}

// ===== DEPOIMENTOS CORRIGIDOS =====
function initTestimonials() {
  const testimonials = document.querySelector('.testimonials');
  const inputs = document.querySelectorAll('.testimonial-input');
  const navLabels = document.querySelectorAll('.testimonial-nav label');
  
  if (!testimonials || inputs.length === 0) return;
  
  let currentIndex = 0;
  let interval;
  let isPaused = false;
  
  // Função para ir para o próximo depoimento
  function nextTestimonial() {
    if (isPaused) return;
    
    currentIndex = (currentIndex + 1) % inputs.length;
    inputs[currentIndex].checked = true;
    updateNavigation();
  }
  
  // Função para ir para um depoimento específico
  function goToTestimonial(index) {
    if (index >= 0 && index < inputs.length) {
      currentIndex = index;
      inputs[currentIndex].checked = true;
      updateNavigation();
    }
  }
  
  // Atualiza a navegação visual
  function updateNavigation() {
    navLabels.forEach((label, index) => {
      if (index === currentIndex) {
        label.classList.add('active');
      } else {
        label.classList.remove('active');
      }
    });
  }
  
  // Inicia o auto-play
  function startAutoPlay() {
    if (interval) clearInterval(interval);
    interval = setInterval(nextTestimonial, CONFIG.animationDelay);
  }
  
  // Para o auto-play
  function stopAutoPlay() {
    if (interval) {
      clearInterval(interval);
      interval = null;
    }
  }
  
  // Event listeners para os inputs radio
  inputs.forEach((input, index) => {
    input.addEventListener('change', () => {
      if (input.checked) {
        currentIndex = index;
        updateNavigation();
        stopAutoPlay();
        setTimeout(startAutoPlay, 1000); // Reinicia após 1 segundo
      }
    });
  });
  
  // Event listeners para os labels de navegação
  navLabels.forEach((label, index) => {
    label.addEventListener('click', (e) => {
      e.preventDefault();
      goToTestimonial(index);
      stopAutoPlay();
      setTimeout(startAutoPlay, 1000); // Reinicia após 1 segundo
    });
  });
  
  // Controles de mouse
  testimonials.addEventListener('mouseenter', () => {
    isPaused = true;
    stopAutoPlay();
  });
  
  testimonials.addEventListener('mouseleave', () => {
    isPaused = false;
    startAutoPlay();
  });
  
  // Controle de visibilidade da página
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      stopAutoPlay();
    } else if (!isPaused) {
      startAutoPlay();
    }
  });
  
  // Controle por teclado (acessibilidade)
  testimonials.addEventListener('keydown', (e) => {
    switch(e.key) {
      case 'ArrowLeft':
        e.preventDefault();
        goToTestimonial(currentIndex > 0 ? currentIndex - 1 : inputs.length - 1);
        stopAutoPlay();
        setTimeout(startAutoPlay, 2000);
        break;
      case 'ArrowRight':
        e.preventDefault();
        goToTestimonial((currentIndex + 1) % inputs.length);
        stopAutoPlay();
        setTimeout(startAutoPlay, 2000);
        break;
    }
  });
  
  // Suporte a touch/swipe (básico)
  let startX = 0;
  let endX = 0;
  
  testimonials.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
    stopAutoPlay();
  });
  
  testimonials.addEventListener('touchend', (e) => {
    endX = e.changedTouches[0].clientX;
    handleSwipe();
    setTimeout(startAutoPlay, 1000);
  });
  
  function handleSwipe() {
    const threshold = 50; // mínimo de pixels para considerar swipe
    const diff = startX - endX;
    
    if (Math.abs(diff) > threshold) {
      if (diff > 0) {
        // Swipe left - próximo
        goToTestimonial((currentIndex + 1) % inputs.length);
      } else {
        // Swipe right - anterior
        goToTestimonial(currentIndex > 0 ? currentIndex - 1 : inputs.length - 1);
      }
    }
  }
  
  // Inicialização
  inputs[0].checked = true; // Garante que o primeiro está selecionado
  updateNavigation();
  startAutoPlay();
  
  // Log para debug
  console.log('Testimonials initialized with', inputs.length, 'items');
}

// ===== UTILITÁRIOS =====
function setMinDate() {
  const dateInput = document.getElementById('data');
  if (dateInput) {
    const today = new Date();
    const tomorrow = new Date(today);
    tomorrow.setDate(tomorrow.getDate() + 1);
    const minDate = tomorrow.toISOString().split('T')[0];
    dateInput.setAttribute('min', minDate);
  }
}

// ===== ANIMAÇÕES =====
function initAnimations() {
  // Intersection Observer para animações sob demanda
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observa elementos animados
  const animatedElements = document.querySelectorAll('.benefit-card, .portfolio-item');
  animatedElements.forEach(el => {
    observer.observe(el);
  });
}

// ===== MELHORIAS DE PERFORMANCE =====
// Debounce para scroll
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Aplicar debounce aos eventos de scroll se necessário
window.addEventListener('scroll', debounce(() => {
  // Código adicional de scroll se necessário
}, 10));

// ===== TRATAMENTO DE ERROS =====
window.addEventListener('error', (e) => {
  console.error('Erro JavaScript:', e.error);
});

// ===== COMPATIBILITY =====
// Polyfill para navegadores mais antigos
if (!Element.prototype.closest) {
  Element.prototype.closest = function(s) {
    var el = this;
    do {
      if (el.matches(s)) return el;
      el = el.parentElement || el.parentNode;
    } while (el !== null && el.nodeType === 1);
    return null;
  };
}