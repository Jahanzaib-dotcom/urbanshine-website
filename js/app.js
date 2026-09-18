/**
 * Urban Shine — Core Interactive Application
 * Providing responsive navigation, dynamic service filters, interactive quote calculator,
 * detailed service modals, booking engine, and WhatsApp dispatch integration.
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initServiceFilters();
  initServiceModal();
  initQuoteCalculator();
  initBookingModal();
  initFaqAccordion();
  initSubpageForms();
  initContactPageForm();
  initBookPage();
  initServicesTabs();
});

/* ==========================================================================
   Service Database (All 12 Services memorized from urbanshinemelb.com.au)
   ========================================================================== */
const SERVICES_DATA = {
  'carpet-cleaning': {
    title: 'Carpet Steam Cleaning',
    category: 'cleaning',
    badge: 'Free Urban Shield™ Included',
    recommended: 'Every 6–12 Months',
    turnaround: '1.5 – 3 Hours (Fast Dry)',
    equipment: 'Industrial Hot Water Extraction',
    shortDesc: 'High-powered steam extraction that lifts embedded dirt, stubborn stains, pet dander, and microscopic allergens deep within carpet fibers without oversaturation.',
    bullets: [
      'Industrial hot water extraction lifts deep-seated grime',
      'Fiber-safe chemistry prevents shrinkage or pile distortion',
      'Neutralizes stubborn pet stains and trapped odours',
      'Includes free Urban Shield™ 99.9% antibacterial barrier'
    ],
    fullDetails: `
      <p>Our deep carpet cleaning system utilizes state-of-the-art truck-mounted and high-pressure portable steam extraction equipment. We don't just wash the surface; we rinse away years of grime, dirt mites, dust particles, and allergens trapped at the base of your carpet pile.</p>
      <h4 style="font-size:1.1rem; font-weight:700; margin:16px 0 8px; color:var(--gray-900);">Why Choose Urban Shine for Carpets:</h4>
      <ul style="list-style:disc; margin-left:20px; line-height:1.7; color:var(--gray-600);">
        <li><strong>Fabric-Specific Detergents:</strong> We inspect wool, nylon, polyester, and blend weaves to choose balanced pH solutions.</li>
        <li><strong>Rapid Moisture Extraction:</strong> Heavy suction leaves carpets only lightly damp, drying fully in just 2 to 4 hours.</li>
        <li><strong>Complimentary Sanitisation:</strong> Every room treated with Urban Shield™ eliminating 99.9% of bacteria.</li>
      </ul>
    `
  },
  'couch-cleaning': {
    title: 'Couch & Upholstery Cleaning',
    category: 'cleaning',
    badge: 'Free Urban Shield™ Included',
    recommended: 'Every 6–12 Months',
    turnaround: '1 – 2 Hours',
    equipment: 'Delicate Low-Moisture Upholstery Tools',
    shortDesc: 'Professional restorative cleaning for fabric and leather lounges, couches, recliners, and dining chairs, eliminating grease, sweat, food spills, and pet odors.',
    bullets: [
      'Tailored solutions for delicate linen, velour, cotton & leather',
      'Specialist spot treatment for wine, coffee, grease & pet marks',
      'Restores original vibrant colors without chemical fading',
      'Includes complimentary Urban Shield™ hygiene seal'
    ],
    fullDetails: `
      <p>Couches endure daily contact with skin oils, food spills, dust, and pet dander. Our technicians carefully inspect your sofa's fabric code and construction before applying gentle pre-conditioning treatments followed by low-moisture steam extraction.</p>
      <h4 style="font-size:1.1rem; font-weight:700; margin:16px 0 8px; color:var(--gray-900);">Upholstery Protection:</h4>
      <p style="color:var(--gray-600); line-height:1.6;">Our extraction process removes hidden allergens lodged deep in sofa foam. With our Urban Shield™ treatment applied afterward, fabrics resist liquid penetration and microbial settlement.</p>
    `
  },
  'curtain-cleaning': {
    title: 'On-Site Curtain Cleaning',
    category: 'cleaning',
    badge: 'Zero Fabric Shrinkage',
    recommended: 'Every 12 Months',
    turnaround: '1 – 2 Hours',
    equipment: 'Drape Extraction Steamers',
    shortDesc: 'Hassle-free on-site drape and curtain steam cleaning without the inconvenience of taking heavy curtains down from their tracks.',
    bullets: [
      '100% on-site convenience — leave curtains hanging on rails',
      'Removes airborne soot, cooking oils, dust mites & odours',
      'Zero shrinkage or fabric wrinkling guaranteed',
      'Suitable for sheers, blockouts, silk blends & heavy velvet'
    ],
    fullDetails: `
      <p>Taking curtains down and sending them to dry cleaners is tedious and often leads to pleated fabric damage. Our high-precision on-site curtain cleaning lifts dust, airborne pollutants, and stubborn odors directly while they hang.</p>
    `
  },
  'mattress-cleaning': {
    title: 'Deep Mattress Sanitisation',
    category: 'cleaning',
    badge: 'Hypoallergenic Sleep Hygiene',
    recommended: 'Every 6 Months',
    turnaround: '45 – 90 Minutes',
    equipment: 'High-Heat Steam & Dust Mite Vacuum',
    shortDesc: 'Eradicates microscopic dust mites, bacteria, dead skin cells, and perspiration stains for a hygienic, restorative, and allergy-free sleep environment.',
    bullets: [
      'Destroys dust mites and neutralizes asthma triggers',
      'Safely extracts sweat, accidental spills & bodily stains',
      'High-heat steam sanitisation with zero residual chemicals',
      'Leaves mattress refreshed, dry, and ready for sleep'
    ],
    fullDetails: `
      <p>An average mattress can harbor millions of dust mites and allergens that compromise respiratory health. Our specialized mattress sanitisation uses hospital-grade dry steam and UV-assisted extraction to neutralize microscopic pests.</p>
    `
  },
  'steam-cleaning': {
    title: 'Chemical-Free Steam Cleaning',
    category: 'cleaning',
    badge: '100% Eco-Safe Sanitisation',
    recommended: 'On Demand / Seasonal',
    turnaround: 'Flexible by Area',
    equipment: 'Superheated Vapour Systems (180°C)',
    shortDesc: 'High-pressure, superheated vapor sanitisation for hard surfaces, bathroom tiles, tapware, and kitchens — zero chemicals, 100% safe for infants and pets.',
    bullets: [
      'Superheated steam kills 99.9% of bacteria and viral particles',
      'Dissolves baked-on kitchen grease and bathroom limescale',
      '100% free of synthetic detergents, fragrances, or residues',
      'Ideal for sensitive allergy sufferers, babies, and indoor pets'
    ],
    fullDetails: `
      <p>Steam cleaning relies solely on high-temperature thermal power rather than corrosive detergents. It melts grime on tiles, grout, stainless steel, and sanitary fixtures while simultaneously sterilizing contact surfaces.</p>
    `
  },
  'floor-polishing': {
    title: 'Floor Refresh & High-Gloss Polishing',
    category: 'floor',
    badge: 'Rapid Refresh • No Downtime',
    recommended: 'Every 12–18 Months',
    turnaround: '2 – 4 Hours',
    equipment: 'Rotary Floor Burnishers & Diamond Pads',
    shortDesc: 'Revives dull, scuffed timber and polished concrete floors, infusing a deep protective gloss layer without the hefty cost and disruption of full sanding.',
    bullets: [
      'Restores rich, reflective sheen to worn floorboards',
      'Adds a resilient protective barrier against foot traffic',
      'Perfect for both solid timber and decorative polished concrete',
      'Extends the lifespan of your existing floor polyurethane'
    ],
    fullDetails: `
      <p>Floor Refresh is our cost-effective alternative to full floor replacement. We mechanically buff away microscopic surface abrasions and apply high-grade protective sealers to restore that warm, rich glow.</p>
    `
  },
  'floor-sanding': {
    title: 'Dust-Free Floor Sanding',
    category: 'floor',
    badge: '99% Dust-Extraction Tech',
    recommended: 'Floors with Scratches & Dents',
    turnaround: '1 – 2 Days',
    equipment: 'HEPA-Filtered Continuous Sanding Units',
    shortDesc: 'Precision timber floor leveling and resurfacing utilizing advanced dust-reduction machinery that keeps your indoor air clean and furniture protected.',
    bullets: [
      'State-of-the-art dust containment system keeps home clean',
      'Smooths out scratches, gouges, pet claw marks & uneven joins',
      'Strips old peeling varnish down to pristine raw timber',
      'Prepares surface perfectly for stains, oils, or polyurethane'
    ],
    fullDetails: `
      <p>Traditional floor sanding creates clouds of airborne wood dust that coat walls and HVAC ducts. Our advanced dust-free equipment captures 99% of dust particles right at the cutting head, ensuring clean and smooth results.</p>
    `
  },
  'floor-restoration': {
    title: 'Complete Floor Restoration',
    category: 'floor',
    badge: 'Heritage & Period Timber Care',
    recommended: 'Heavily Damaged / Aged Floors',
    turnaround: '2 – 3 Days',
    equipment: 'Comprehensive Woodworking & Planing Rig',
    shortDesc: 'Comprehensive architectural repair for aging or damaged timber floors, including loose board refastening, timber replacements, gap filling, and commercial coating.',
    bullets: [
      'Repairs split, cupped, or rotting floorboards with matched timber',
      'Seamless resin gap filling for smooth draft-free floors',
      'Specialized care for WA heritage Jarrah, Blackbutt & Pine',
      'Commercial-grade polyurethane or organic oil finishes'
    ],
    fullDetails: `
      <p>Designed for historic homes in Cottesloe, Peppermint Grove, and Claremont. We meticulously restore original timber character rather than covering it up, increasing your home\'s appraised market value.</p>
    `
  },
  'tile-grout-cleaning': {
    title: 'Tile & Grout Deep Extraction',
    category: 'floor',
    badge: 'Penetrating Rotary Scrub',
    recommended: 'Every 12 Months',
    turnaround: '1.5 – 3 Hours',
    equipment: 'Enclosed High-Pressure Rotary Extractor',
    shortDesc: 'High-pressure enclosed rotary scrubbing that extracts stubborn grime, black mold, and deep grease from porous grout lines that conventional mopping cannot move.',
    bullets: [
      'Porous grout deep clean — extracts embedded black mold & mildew',
      'Restores natural grout lines and ceramic/porcelain luster',
      'Enclosed vacuum dome prevents overspray or messy splashbacks',
      'Optional protective penetrating sealer to repel future spills'
    ],
    fullDetails: `
      <p>Grout is porous and acts like a magnet for mop water contaminants. Our 1000 PSI rotary tool flushes out deep residues while simultaneously extracting the waste water, leaving floors sanitized and dry.</p>
    `
  },
  'decking-restoration': {
    title: 'Outdoor Timber Decking Restoration',
    category: 'outdoor',
    badge: 'UV & Rain Weatherproofing',
    recommended: 'Every 12–24 Months',
    turnaround: '1 – 2 Days',
    equipment: 'Heavy-Duty Deck Stripper & Sanders',
    shortDesc: 'Restores weathered, grey, and splintered outdoor entertaining decks. Includes deep power sanding, structural board repairs, and premium UV-protective oiling.',
    bullets: [
      'Strips stubborn grey oxidation and flaking old stains',
      'Eliminates dangerous splinters and countersinks popping screws',
      'High-solids penetrating decking oil protects against harsh WA sun',
      'Enhances outdoor entertaining appeal and property kerb value'
    ],
    fullDetails: `
      <p>Perth\'s high UV index and winter rains quickly erode timber decks. We strip back damaged timber fibres, sand boards smooth, and infuse deeply penetrating timber oils that nourish and protect against splitting.</p>
    `
  },
  'aircon-cleaning': {
    title: 'Split System Aircon Sanitisation',
    category: 'maintenance',
    badge: 'Under 1 Hour • Instant Efficiency',
    recommended: 'Every 6–12 Months',
    turnaround: 'Under 60 Mins / Unit',
    equipment: 'Pressurized Coil Flushing & Catch Bag Rig',
    shortDesc: 'Comprehensive evaporator coil, fan barrel, and filter decontamination that removes toxic black mold, bacterial slime, and dust choke-points to slash energy bills.',
    bullets: [
      'Flushes toxic mold and bacterial sludge from indoor coils',
      'Eliminates musty, stale AC odors from the very first turn-on',
      'Restores clean airflow and reduces compressor strain & power bills',
      'Mess-free service with specialized protective wall catch-bags'
    ],
    fullDetails: `
      <p>Moisture inside air conditioning units creates an ideal breeding ground for mold and legionella spores. We mount a custom catch-bag, wash coils with antibacterial solution, and thoroughly flush the blower fan wheel.</p>
    `
  },
  'flood-restoration': {
    title: '24/7 Emergency Flood Treatment',
    category: 'emergency',
    badge: '24/7 Rapid Mobile Response',
    recommended: 'Immediate Emergency',
    turnaround: '24/7 Immediate Dispatch',
    equipment: 'Submersible Pumps & Commercial Dehumidifiers',
    shortDesc: 'Around-the-clock emergency response for pipe bursts, appliance overflows, and storm flooding. Rapid high-volume water extraction and structural drying.',
    bullets: [
      '24/7 emergency hotline with immediate Perth dispatch',
      'High-volume water extraction minimizes deep structural damage',
      'Industrial LGR dehumidifiers and high-velocity turbo air movers',
      'Antimicrobial spray treatments prevent hazardous mold infestations'
    ],
    fullDetails: `
      <p>Water damage escalates every hour. Within 24-48 hours, mold colonies establish. Our emergency crew extracts standing water, sets up structural drying chambers, and treats all affected materials with hospital-grade fungicides.</p>
    `
  }
};

/* ==========================================================================
   Navigation & Sticky Header
   ========================================================================== */
function initNavigation() {
  const header = document.querySelector('.main-header') || document.querySelector('.site-header');
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.primary-nav') || document.querySelector('.nav-menu');

  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 30) {
        header.classList.add('is-scrolled');
      } else {
        header.classList.remove('is-scrolled');
      }
    });
  }

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('is-open');
    });

    // Close when clicking nav links
    navMenu.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        navMenu.classList.remove('is-open');
      });
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId === '') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const headerOffset = 80;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

/* ==========================================================================
   Service Filtering
   ========================================================================== */
function initServiceFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const serviceCards = document.querySelectorAll('.service-card, .service-photo-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      serviceCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'flex';
          card.style.opacity = '1';
        } else {
          card.style.display = 'none';
          card.style.opacity = '0';
        }
      });
    });
  });
}

/* ==========================================================================
   Service Details Modal
   ========================================================================== */
function initServiceModal() {
  const modalOverlay = document.getElementById('serviceModalOverlay');
  const modalTitle = document.getElementById('serviceModalTitle');
  const modalBody = document.getElementById('serviceModalBody');
  const modalBookBtn = document.getElementById('serviceModalBookBtn');
  const closeBtn = document.getElementById('serviceModalCloseBtn');

  if (!modalOverlay) return;

  document.querySelectorAll('.open-service-modal').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const serviceKey = btn.getAttribute('data-service');
      const data = SERVICES_DATA[serviceKey];
      if (!data) return;

      modalTitle.textContent = data.title;
      modalBody.innerHTML = `
        <div class="detail-meta-grid">
          <div class="meta-item">
            <div class="meta-item-label">Recommended Frequency</div>
            <div class="meta-item-val">${data.recommended}</div>
          </div>
          <div class="meta-item">
            <div class="meta-item-label">Service Turnaround</div>
            <div class="meta-item-val">${data.turnaround}</div>
          </div>
          <div class="meta-item">
            <div class="meta-item-label">Equipment Used</div>
            <div class="meta-item-val">${data.equipment}</div>
          </div>
        </div>
        <p style="font-size:1.05rem; font-weight:500; color:var(--gray-800); margin-bottom:16px;">
          ${data.shortDesc}
        </p>
        <div style="background:var(--gray-50); padding:16px 20px; border-radius:var(--radius-md); margin-bottom:20px; border-left:4px solid var(--accent-primary);">
          <div style="font-weight:700; color:var(--gray-900); margin-bottom:8px;">Core Service Scope:</div>
          <ul style="display:flex; flex-direction:column; gap:8px;">
            ${data.bullets.map(b => `<li style="display:flex; align-items:center; gap:8px; font-size:0.9rem; color:var(--gray-700);"><span style="color:#059669; font-weight:bold;">✓</span> ${b}</li>`).join('')}
          </ul>
        </div>
        ${data.fullDetails}
      `;

      modalBookBtn.onclick = () => {
        closeModal(modalOverlay);
        openBookingModal(serviceKey);
      };

      openModal(modalOverlay);
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => closeModal(modalOverlay));
  }

  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) closeModal(modalOverlay);
  });
}

/* ==========================================================================
   Interactive Quote Calculator
   ========================================================================== */
function initQuoteCalculator() {
  const priceMinEl = document.getElementById('calcPriceMin');
  const priceMaxEl = document.getElementById('calcPriceMax');
  const summaryList = document.getElementById('calcSummaryItems');
  if (!priceMinEl || !priceMaxEl || !summaryList) return;

  const carpetOptions = document.querySelectorAll('[data-calc-carpet]');
  const couchOptions = document.querySelectorAll('[data-calc-couch]');
  const acOptions = document.querySelectorAll('[data-calc-ac]');
  const tileOptions = document.querySelectorAll('[data-calc-tile]');
  const calcLockBtn = document.getElementById('calcLockBtn');

  let state = {
    carpet: 3,     // 3 rooms
    couch: 3,      // 3-seater
    ac: 1,         // 1 split unit
    tile: 0        // 0 tile
  };

  function updateActiveChips(group, valueAttr, currentVal) {
    group.forEach(chip => {
      const val = parseInt(chip.getAttribute(valueAttr), 10);
      if (val === currentVal) {
        chip.classList.add('selected');
      } else {
        chip.classList.remove('selected');
      }
    });
  }

  function recalculate() {
    let min = 0;
    let max = 0;
    let items = [];

    // Carpet Pricing ($35 - $45 per room, base callout $99)
    if (state.carpet > 0) {
      const cMin = Math.max(99, state.carpet * 38);
      const cMax = Math.max(130, state.carpet * 48);
      min += cMin;
      max += cMax;
      items.push(`${state.carpet} Carpeted Room${state.carpet > 1 ? 's' : ''} (Incl. Urban Shield™)`);
    }

    // Couch Pricing (2-seat: $90, 3-seat: $130, 5-seat L: $190)
    if (state.couch > 0) {
      if (state.couch === 2) { min += 85; max += 110; items.push('2-Seater Fabric / Leather Couch'); }
      if (state.couch === 3) { min += 120; max += 150; items.push('3-Seater Family Lounge (Incl. Sanitisation)'); }
      if (state.couch === 5) { min += 180; max += 230; items.push('5-Seater Modular / L-Shape Lounge'); }
    }

    // Aircon Pricing ($85 - $110 per split unit)
    if (state.ac > 0) {
      min += state.ac * 85;
      max += state.ac * 115;
      items.push(`${state.ac} Aircon Split System${state.ac > 1 ? 's' : ''} Deep Flush`);
    }

    // Tile Area Pricing ($5 - $7 per m²)
    if (state.tile > 0) {
      min += state.tile * 4.8;
      max += state.tile * 6.5;
      items.push(`${state.tile}m² Rotary Tile & Grout Extraction`);
    }

    if (min === 0) {
      min = 99;
      max = 149;
      items.push('Base Service Callout / Assessment');
    }

    priceMinEl.textContent = `$${Math.round(min)}`;
    priceMaxEl.textContent = `$${Math.round(max)}`;

    summaryList.innerHTML = items.map(item => `
      <div class="calc-include-item">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
        <span>${item}</span>
      </div>
    `).join('');
  }

  carpetOptions.forEach(c => c.addEventListener('click', () => {
    state.carpet = parseInt(c.getAttribute('data-calc-carpet'), 10);
    updateActiveChips(carpetOptions, 'data-calc-carpet', state.carpet);
    recalculate();
  }));

  couchOptions.forEach(c => c.addEventListener('click', () => {
    state.couch = parseInt(c.getAttribute('data-calc-couch'), 10);
    updateActiveChips(couchOptions, 'data-calc-couch', state.couch);
    recalculate();
  }));

  acOptions.forEach(c => c.addEventListener('click', () => {
    state.ac = parseInt(c.getAttribute('data-calc-ac'), 10);
    updateActiveChips(acOptions, 'data-calc-ac', state.ac);
    recalculate();
  }));

  tileOptions.forEach(c => c.addEventListener('click', () => {
    state.tile = parseInt(c.getAttribute('data-calc-tile'), 10);
    updateActiveChips(tileOptions, 'data-calc-tile', state.tile);
    recalculate();
  }));

  if (calcLockBtn) {
    calcLockBtn.addEventListener('click', () => {
      const summaryText = `Estimated Range: ${priceMinEl.textContent} - ${priceMaxEl.textContent}. Scope: ${state.carpet} rooms carpet, ${state.couch}-seat couch, ${state.ac} AC units, ${state.tile}m2 tile.`;
      openBookingModal('custom', summaryText);
    });
  }

  recalculate();
}

/* ==========================================================================
   Booking Modal & Submission Flow
   ========================================================================== */
function initBookingModal() {
  const modalOverlay = document.getElementById('bookingModalOverlay');
  if (!modalOverlay) return;
  const closeBtn = document.getElementById('bookingModalCloseBtn');
  const bookingForm = document.getElementById('bookingForm');
  const serviceSelect = document.getElementById('bookingServiceSelect');
  const notesField = document.getElementById('bookingNotes');

  const successOverlay = document.getElementById('successModalOverlay');
  const successCloseBtn = document.getElementById('successModalCloseBtn');
  const successWhatsAppBtn = document.getElementById('successWhatsAppBtn');

  // Trigger buttons across page
  document.querySelectorAll('.open-booking-modal').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const service = btn.getAttribute('data-service') || 'carpet-cleaning';
      openBookingModal(service);
    });
  });

  window.openBookingModal = function(serviceKey, customNotes = '') {
    if (serviceSelect && serviceKey && serviceKey !== 'custom') {
      serviceSelect.value = serviceKey;
    }
    if (notesField && customNotes) {
      notesField.value = customNotes;
    }
    openModal(modalOverlay);
  };

  if (closeBtn) {
    closeBtn.addEventListener('click', () => closeModal(modalOverlay));
  }

  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) closeModal(modalOverlay);
  });

  if (bookingForm) {
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = document.getElementById('bookName').value.trim();
      const phone = document.getElementById('bookPhone').value.trim();
      const email = document.getElementById('bookEmail').value.trim();
      const suburb = document.getElementById('bookSuburb').value.trim();
      const service = serviceSelect.options[serviceSelect.selectedIndex].text;

      if (!name || !phone) {
        alert('Please provide your name and contact phone number.');
        return;
      }

      // Automatically route enquiry to Admin Panel
      if (window.UrbanShineLeads) {
        window.UrbanShineLeads.addLead({
          name: name,
          phone: phone,
          email: email,
          suburb: suburb,
          service: service,
          source: 'Homepage Booking Modal'
        });
      }

      // Close booking modal
      closeModal(modalOverlay);

      // Setup WhatsApp click-through on success
      const waMsg = encodeURIComponent(`Hello Urban Shine, I have just submitted a quote request.\nName: ${name}\nPhone: ${phone}\nSuburb: ${suburb}\nService: ${service}\nEmail: ${email}`);
      if (successWhatsAppBtn) {
        successWhatsAppBtn.href = `https://wa.me/61432979551?text=${waMsg}`;
      }

      // Show success modal
      openModal(successOverlay);
      bookingForm.reset();
    });
  }

  if (successCloseBtn) {
    successCloseBtn.addEventListener('click', () => closeModal(successOverlay));
  }

  if (successOverlay) {
    successOverlay.addEventListener('click', (e) => {
      if (e.target === successOverlay) closeModal(successOverlay);
    });
  }
}

/* ==========================================================================
   FAQ Accordion
   ========================================================================== */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const header = item.querySelector('.faq-header');
    const body = item.querySelector('.faq-body');

    header.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all other FAQs
      faqItems.forEach(other => {
        other.classList.remove('active');
        other.querySelector('.faq-body').style.maxHeight = null;
      });

      if (!isActive) {
        item.classList.add('active');
        body.style.maxHeight = body.scrollHeight + 'px';
      }
    });
  });
}

/* ==========================================================================
   Modal Helpers
   ========================================================================== */
function openModal(overlay) {
  overlay.classList.add('is-active');
  document.body.style.overflow = 'hidden';
}

function closeModal(overlay) {
  overlay.classList.remove('is-active');
  document.body.style.overflow = '';
}

/* ==========================================================================
   Subpage Interactive Quote Forms & Dynamic Pricing
   ========================================================================== */
function initSubpageForms() {
  const sidebarForms = document.querySelectorAll('.sidebar-quote-form');

  sidebarForms.forEach(form => {
    const card = form.closest('.sidebar-form-card');
    const priceAmountEl = card ? card.querySelector('.sidebar-price-amount span.price-val') : null;
    const scopePills = form.querySelectorAll('.scope-pill');

    // Scope pill click handler
    scopePills.forEach(pill => {
      pill.addEventListener('click', () => {
        scopePills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');

        const radio = pill.querySelector('input[type="radio"]');
        if (radio) radio.checked = true;

        const price = pill.getAttribute('data-price');
        if (priceAmountEl && price) {
          priceAmountEl.textContent = price;
        }
      });
    });

    // Form submission handler
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const nameInput = form.querySelector('[name="client_name"]');
      const phoneInput = form.querySelector('[name="client_phone"]');
      const suburbInput = form.querySelector('[name="client_suburb"]');
      const dateInput = form.querySelector('[name="service_date"]');
      const serviceName = form.getAttribute('data-service-title') || 'Cleaning Service';

      const name = nameInput ? nameInput.value.trim() : '';
      const phone = phoneInput ? phoneInput.value.trim() : '';
      const suburb = suburbInput ? suburbInput.value.trim() : 'Perth Metro';
      const date = dateInput ? dateInput.value : 'Soonest Available';

      let selectedScope = 'Standard Scope';
      const activePill = form.querySelector('.scope-pill.active .scope-pill-title');
      if (activePill) {
        selectedScope = activePill.textContent.trim();
      }

      let estPrice = '';
      if (priceAmountEl) {
        estPrice = priceAmountEl.textContent.trim();
      }

      if (!name || !phone) {
        alert('Please enter your full name and Australian mobile phone number.');
        return;
      }

      // Automatically route enquiry to Admin Panel
      if (window.UrbanShineLeads) {
        window.UrbanShineLeads.addLead({
          name: name,
          phone: phone,
          suburb: suburb,
          service: serviceName,
          scope: selectedScope,
          date: date,
          source: 'Service Page Sidebar Quote'
        });
      }

      // Pre-filled WhatsApp message
      const textMsg = encodeURIComponent(
        `Hello Urban Shine Perth! 👋\n` +
        `I would like to request an on-site assessment and quote:\n\n` +
        `• Service: ${serviceName}\n` +
        `• Scope: ${selectedScope}\n` +
        `• Assessment Type: Free On-Site Quote (Zero Travel Surcharges)\n` +
        `• Preferred Date: ${date}\n` +
        `• Suburb: ${suburb}\n` +
        `• Customer: ${name}\n` +
        `• Contact Phone: ${phone}\n\n` +
        `Please confirm technician availability.`
      );

      const waUrl = `https://wa.me/61432979551?text=${textMsg}`;

      // Show success state inside the card
      const formContainer = form.parentElement;
      form.style.display = 'none';

      const successBox = document.createElement('div');
      successBox.className = 'form-success-banner';
      successBox.innerHTML = `
        <div class="form-success-icon">✓</div>
        <div class="form-success-title">Priority Assessment Logged!</div>
        <p class="form-success-desc">
          Thank you, <strong>${name}</strong>. Your ${serviceName} request in <strong>${suburb}</strong> has been prioritized. Our dispatch supervisor will phone you on <strong>${phone}</strong> shortly.
        </p>
        <div style="display:flex; flex-direction:column; gap:8px; margin-top:14px;">
          <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="whatsapp-dispatch-btn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
            Connect on WhatsApp Now
          </a>
          <a href="/admin" class="btn btn-outline" style="padding:10px 14px; font-weight:600; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px; font-size:0.88rem;">
            View in Admin Panel →
          </a>
        </div>
      `;
      formContainer.appendChild(successBox);
    });
  });
}

/* ==========================================================================
   Contact Us Page Form Handler
   ========================================================================== */
function initContactPageForm() {
  const contactForm = document.getElementById('contactPageForm');
  if (!contactForm) return;

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('contactName').value.trim();
    const email = document.getElementById('contactEmail').value.trim();
    const phone = document.getElementById('contactPhone').value.trim();
    const service = document.getElementById('contactService').value;
    const urgency = document.getElementById('contactUrgency').value;
    const suburb = document.getElementById('contactSuburb').value.trim();
    const message = document.getElementById('contactMessage').value.trim();

    if (!name || !phone) {
      alert('Please fill in your name and contact phone number.');
      return;
    }

    // Automatically route enquiry to Admin Panel
    if (window.UrbanShineLeads) {
      window.UrbanShineLeads.addLead({
        name: name,
        email: email,
        phone: phone,
        service: service,
        urgency: urgency,
        suburb: suburb,
        notes: message,
        source: 'Contact Us Page Form'
      });
    }

    const waMsg = encodeURIComponent(
      `Hello Urban Shine!\n` +
      `New Website Contact Form Submission:\n\n` +
      `• Name: ${name}\n` +
      `• Phone: ${phone}\n` +
      `• Email: ${email}\n` +
      `• Service: ${service}\n` +
      `• Urgency: ${urgency}\n` +
      `• Suburb: ${suburb}\n` +
      `• Message: ${message}`
    );

    const waUrl = `https://wa.me/61432979551?text=${waMsg}`;

    contactForm.innerHTML = `
      <div class="form-success-banner" style="margin-top:0;">
        <div class="form-success-icon">✓</div>
        <div class="form-success-title">Message Sent Successfully!</div>
        <p class="form-success-desc">
          Thank you <strong>${name}</strong>. Our Perth customer care team has received your message regarding <strong>${service}</strong>. We will contact you at <strong>${phone}</strong> shortly.
        </p>
        <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap; max-width:440px; margin:0 auto;">
          <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="whatsapp-dispatch-btn" style="flex:1; min-width:180px;">
            Connect on WhatsApp
          </a>
          <a href="/admin" class="btn btn-outline" style="padding:10px 18px; font-weight:600; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px; flex:1; min-width:180px;">
            View in Admin Panel →
          </a>
        </div>
      </div>
    `;
  });
}

/* ==========================================================================
   Services Hub Filter Tabs
   ========================================================================== */
function initServicesTabs() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const serviceCards = document.querySelectorAll('.service-directory-card');

  if (!tabBtns.length || !serviceCards.length) return;

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-tab');

      serviceCards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* ==========================================================================
   Booking Page (book.html) Interactive Engine
   ========================================================================== */
function initBookPage() {
  const bookForm = document.getElementById('assessmentBookingForm');
  if (!bookForm) return;

  const serviceSelect = document.getElementById('bookPageService');
  const scopeSelect = document.getElementById('bookPageScope');
  const priceDisplay = document.getElementById('bookPagePrice');

  function updateBookPrice() {
    if (!priceDisplay) return;
    priceDisplay.textContent = 'Free On-Site Assessment (Transparent Quote)';
  }

  if (serviceSelect) serviceSelect.addEventListener('change', updateBookPrice);
  if (scopeSelect) scopeSelect.addEventListener('change', updateBookPrice);
  updateBookPrice();

  bookForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('bookPageName').value.trim();
    const phone = document.getElementById('bookPagePhone').value.trim();
    const email = document.getElementById('bookPageEmail').value.trim();
    const suburb = document.getElementById('bookPageSuburb').value.trim();
    const service = serviceSelect.options[serviceSelect.selectedIndex].text;
    const preferredDate = document.getElementById('bookPageDate').value;
    const preferredSlot = document.getElementById('bookPageSlot').value;
    const notes = document.getElementById('bookPageNotes').value.trim();
    const currentPrice = priceDisplay.textContent;

    if (!name || !phone) {
      alert('Please provide your name and contact phone number.');
      return;
    }

    // Automatically route enquiry to Admin Panel
    if (window.UrbanShineLeads) {
      window.UrbanShineLeads.addLead({
        name: name,
        phone: phone,
        email: email,
        suburb: suburb,
        service: service,
        scope: currentPrice,
        date: preferredDate,
        time: preferredSlot,
        notes: notes,
        source: 'Book Online Page'
      });
    }

    const waMsg = encodeURIComponent(
      `Hello Urban Shine Perth! 👋\n` +
      `New Booking / Assessment Request:\n\n` +
      `• Service: ${service}\n` +
      `• Assessment Type: ${currentPrice}\n` +
      `• Preferred Date: ${preferredDate} (${preferredSlot})\n` +
      `• Suburb: ${suburb}\n` +
      `• Customer: ${name}\n` +
      `• Phone: ${phone}\n` +
      `• Email: ${email}\n` +
      `• Special Notes: ${notes}\n\n` +
      `Please lock in this appointment.`
    );

    const waUrl = `https://wa.me/61432979551?text=${waMsg}`;

    bookForm.innerHTML = `
      <div class="form-success-banner" style="padding:40px 24px;">
        <div class="form-success-icon">✓</div>
        <div class="form-success-title" style="font-size:1.5rem;">Booking Assessment Received!</div>
        <p class="form-success-desc" style="font-size:1rem; max-width:560px; margin:0 auto 24px auto;">
          Thank you, <strong>${name}</strong>. Your appointment request for <strong>${service}</strong> in <strong>${suburb}</strong> has been logged. Our operations manager will call <strong>${phone}</strong> within 15 minutes to confirm technician arrival.
        </p>
        <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap; max-width:440px; margin:0 auto;">
          <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="whatsapp-dispatch-btn" style="flex:1; min-width:180px;">
            Confirm on WhatsApp
          </a>
          <a href="/admin" class="btn btn-outline" style="padding:10px 18px; font-weight:600; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px; flex:1; min-width:180px;">
            View in Admin Panel →
          </a>
        </div>
      </div>
    `;
  });
}
