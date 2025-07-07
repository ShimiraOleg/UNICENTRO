document.addEventListener('DOMContentLoaded', function() {
  initTheme();
  initNavigation();
  initTestimonials();
  initForm();
  initDateInput();
});

function initTheme() {
  const themeButton = document.querySelector('.theme-toggle');
  const themeIcon = document.querySelector('.theme-icon');
  
  if (!themeButton || !themeIcon) return;
  
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const isDark = savedTheme === 'dark' || (!savedTheme && prefersDark);
  
  updateTheme(isDark);
    themeButton.addEventListener('click', function() {
    const currentlyDark = document.documentElement.classList.contains('dark');
    const newTheme = !currentlyDark;
    updateTheme(newTheme);
    localStorage.setItem('theme', newTheme ? 'dark' : 'light');
  });
  
  function updateTheme(isDark) {
    if (isDark) {
      document.documentElement.classList.add('dark');
      themeIcon.textContent = '☀️';
    } else {
      document.documentElement.classList.remove('dark');
      themeIcon.textContent = '🌙';
    }
  }
}

function initNavigation() {
  const header = document.querySelector('.header');
  const navLinks = document.querySelectorAll('.nav__link');
  const sections = document.querySelectorAll('section[id]');
  
  if (!header) return;
  
  window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    
    updateActiveLink();
  });
  
  navLinks.forEach(function(link) {
    link.addEventListener('click', function(e) {
      const href = link.getAttribute('href');
      
      if (href && href.startsWith('#')) {
        e.preventDefault();
        const targetSection = document.querySelector(href);
        
        if (targetSection) {
          const headerHeight = header.offsetHeight;
          const targetPosition = targetSection.offsetTop - headerHeight;
          
          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });
        }
      }
    });
  });
  
  function updateActiveLink() {
    const scrollPosition = window.scrollY + 100;
    let currentSection = '';
    
    sections.forEach(function(section) {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');
      
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        currentSection = sectionId;
      }
    });
    
    navLinks.forEach(function(link) {
      link.classList.remove('active');
    });
    
    if (currentSection) {
      const activeLink = document.querySelector('.nav__link[href="#' + currentSection + '"]');
      if (activeLink) {
        activeLink.classList.add('active');
      }
    }
  }
  
  updateActiveLink();
}

function initTestimonials() {
  const testimonialInputs = document.querySelectorAll('.testimonial-input');
  const testimonialLabels = document.querySelectorAll('.testimonial-nav label');
  const testimonialsContainer = document.querySelector('.testimonials');
  
  if (testimonialInputs.length === 0) return;
  
  let currentTestimonial = 0;
  let autoplayTimer = null;
  
  function goToTestimonial(index) {
    if (index < 0 || index >= testimonialInputs.length) return;
    
    currentTestimonial = index;
    
    testimonialInputs[currentTestimonial].checked = true;
    
    testimonialLabels.forEach(function(label, i) {
      if (i === currentTestimonial) {
        label.classList.add('active');
      } else {
        label.classList.remove('active');
      }
    });
  }
  
  function nextTestimonial() {
    const nextIndex = (currentTestimonial + 1) % testimonialInputs.length;
    goToTestimonial(nextIndex);
  }
  
  function startAutoplay() {
    stopAutoplay();
    autoplayTimer = setInterval(nextTestimonial, 5000);
  }
  
  function stopAutoplay() {
    if (autoplayTimer) {
      clearInterval(autoplayTimer);
      autoplayTimer = null;
    }
  }
  
  testimonialLabels.forEach(function(label, index) {
    label.addEventListener('click', function() {
      goToTestimonial(index);
      stopAutoplay();
      setTimeout(startAutoplay, 3000);
    });
  });
  
  if (testimonialsContainer) {
    testimonialsContainer.addEventListener('mouseenter', stopAutoplay);
    testimonialsContainer.addEventListener('mouseleave', startAutoplay);
  }
  
  goToTestimonial(0);
  startAutoplay();
}

function initForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;
  
  const phoneInput = document.getElementById('telefone');
  if (phoneInput) {
    phoneInput.addEventListener('input', function(e) {
      let value = e.target.value.replace(/\D/g, '');
      
      if (value.length >= 11) {
        value = value.replace(/^(\d{2})(\d{5})(\d{4}).*/, '($1) $2-$3');
      } else if (value.length >= 6) {
        value = value.replace(/^(\d{2})(\d{4})(\d{0,4})/, '($1) $2-$3');
      } else if (value.length >= 2) {
        value = value.replace(/^(\d{2})(\d{0,5})/, '($1) $2');
      }
      
      e.target.value = value;
    });
  }
  
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const submitButton = form.querySelector('button[type="submit"]');
    const successMessage = form.querySelector('.form-success');
    const originalText = submitButton.textContent;
    
    submitButton.textContent = 'Enviando...';
    submitButton.disabled = true;
    
    setTimeout(function() {
      if (successMessage) {
        successMessage.hidden = false;
        successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      
      form.reset();
      
      submitButton.textContent = originalText;
      submitButton.disabled = false;
      
      setTimeout(function() {
        if (successMessage) {
          successMessage.hidden = true;
        }
      }, 5000);
    }, 2000);
  });
}

function initDateInput() {
  const dateInput = document.getElementById('data');
  if (dateInput) {
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const minDate = tomorrow.toISOString().split('T')[0];
    dateInput.setAttribute('min', minDate);
  }
}