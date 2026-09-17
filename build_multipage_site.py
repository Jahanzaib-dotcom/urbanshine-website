#!/usr/bin/env python3
import os
import re

SITE_DIR = "/Users/JahanzaibDev/urbanshine-website"
CONTEXT_DIR = "/Users/JahanzaibDev/urbanshine_site_context/pages"

SERVICES_META = [
    {
        "slug": "carpet-cleaning-perth",
        "file": "carpet-cleaning-perth.md",
        "title_short": "Carpet Cleaning",
        "h1": "Professional Carpet Steam Cleaning",
        "meta_title": "Carpet Cleaning Perth | Deep Steam & Urban Shield™ | Urban Shine",
        "meta_desc": "Urban Shine delivers professional carpet steam cleaning in Perth. Hot water extraction, stain & odour removal, 14-day guarantee & free Urban Shield™ sanitisation.",
        "image": "assets/images/services/carpet-cleaning.png",
        "category": "cleaning",
        "badge": "Free Urban Shield™ 99.9% Included",
        "turnaround": "1.5 – 3 Hours (Fast Drying)",
        "equipment": "Industrial Hot Water Extraction & Rotary Wands",
        "meta_tag": "Free Urban Shield™ Included",
        "pills": [
            {"title": "1-2 Rooms", "desc": "Up to 25m²"},
            {"title": "3 Rooms Standard", "desc": "Approx 45m²", "active": True},
            {"title": "4 Rooms + Hall", "desc": "Approx 65m²"},
            {"title": "5+ Rooms / Whole House", "desc": "85m²+"}
        ],
        "faqs": [
            ("How long do carpets take to dry after steam cleaning?", "With our industrial high-velocity extraction, carpets typically dry in 2 to 4 hours. Adequate airflow or running ceiling fans speeds this up even further."),
            ("Can you remove old, stubborn pet stains and odours?", "Yes, our multi-stage treatment includes targeted enzyme breaking agents and sub-surface rinsing to neutralize uric acids and deep trapped odours."),
            ("What is the free Urban Shield™ application?", "Urban Shield™ is an Australian-developed hospital-grade antimicrobial treatment applied to every clean. It eradicates 99.9% of bacteria and creates a barrier against mould regrowth."),
            ("Do you move furniture before cleaning?", "We gladly slide light furniture (chairs, small tables, sofas) and clean thoroughly underneath, replacing them with protective tabs.")
        ]
    },
    {
        "slug": "couch-cleaning-perth",
        "file": "couch-cleaning-perth.md",
        "title_short": "Couch Cleaning",
        "h1": "Professional Couch & Upholstery Cleaning",
        "meta_title": "Couch & Upholstery Cleaning Perth | Urban Shine Perth",
        "meta_desc": "Specialist couch and lounge steam cleaning in Perth. Fabric and leather upholstery care, stain removal, odour neutralisation and free Urban Shield™ protection.",
        "image": "assets/images/services/couch-cleaning.png",
        "category": "cleaning",
        "badge": "Zero Fabric Shrinkage Guaranteed",
        "turnaround": "1 – 2 Hours",
        "equipment": "Low-Moisture Delicate Upholstery Extraction & Steam Injection",
        "meta_tag": "Zero Shrinkage Guarantee",
        "pills": [
            {"title": "2-Seater Lounge", "desc": "Fabric or Leather"},
            {"title": "3-Seater Family Sofa", "desc": "Standard Lounge", "active": True},
            {"title": "5-Seater L-Shape", "desc": "Modular / Chaise"},
            {"title": "Dining Chairs & Armchairs", "desc": "Set of 6 Chairs"}
        ],
        "faqs": [
            ("Do you clean both fabric and leather couches?", "Yes! Our technicians are trained in fabric identification (cotton, polyester, linen, velvet) and delicate leather conditioning to prevent cracking and fading."),
            ("How soon can we sit on the couch after cleaning?", "Most couches dry within 2 to 3 hours thanks to our low-moisture extraction heads."),
            ("Will steam cleaning remove body oils and perspiration?", "Yes, our pre-treatment emulsifies skin oils, sweat marks, and food stains, lifting them out completely during steam extraction."),
            ("Is the treatment safe for children and indoor pets?", "100% safe. We only use non-toxic, eco-certified formulations with zero harsh chemical residues.")
        ]
    },
    {
        "slug": "curtain-cleaning-perth",
        "file": "curtain-cleaning-perth.md",
        "title_short": "Curtain Cleaning",
        "h1": "On-Site Curtain & Drape Steam Cleaning",
        "meta_title": "On-Site Curtain Cleaning Perth | Zero Shrinkage | Urban Shine",
        "meta_desc": "Professional curtain cleaning on-site in Perth. No need to take curtains down. Gentle steam extraction for sheers, drapes, and blockouts.",
        "image": "assets/images/services/curtain-cleaning.png",
        "category": "cleaning",
        "badge": "100% On-Site Convenience",
        "turnaround": "1 – 2 Hours",
        "equipment": "Continuous Drape Vapor Steamers & Pleat Groomers",
        "meta_tag": "100% On-Site Service",
        "pills": [
            {"title": "1-2 Curtain Sets", "desc": "Single Room"},
            {"title": "3-4 Curtain Sets", "desc": "Living & Bedrooms", "active": True},
            {"title": "5-6 Window Sets", "desc": "Whole Standard Home"},
            {"title": "Floor-to-Ceiling Luxury Drapes", "desc": "Velvet / Heavy Weave"}
        ],
        "faqs": [
            ("Do I have to take curtains down from their tracks?", "Not at all! Our entire process is conducted on-site while your curtains hang in place, preserving pleats and hooks."),
            ("Will my curtains shrink or stretch?", "No. Our low-moisture vapor technology is calibrated specifically to avoid fabric distortion or shrinkage."),
            ("Does it remove cooking odours and dust mites?", "Yes, the superheated vapor dissolves airborne oils, dust mite waste, and neutralizes pet or smoke odours."),
            ("Can sheer and delicate fabrics be cleaned safely?", "Yes, our technicians test each fabric first to adjust heat and suction levels accordingly.")
        ]
    },
    {
        "slug": "mattress-cleaning-perth",
        "file": "mattress-cleaning-perth.md",
        "title_short": "Mattress Cleaning",
        "h1": "Deep Mattress Cleaning & Sanitisation",
        "meta_title": "Mattress Cleaning Perth | Allergen & Dust Mite Removal | Urban Shine",
        "meta_desc": "Deep mattress cleaning and hospital-grade sanitisation in Perth. Eradicates dust mites, sweat stains, and bacteria for a hygienic sleep sanctuary.",
        "image": "assets/images/services/mattress-cleaning.png",
        "category": "cleaning",
        "badge": "Hypoallergenic Sleep Hygiene",
        "turnaround": "45 – 90 Minutes",
        "equipment": "High-Heat Sanitising Vacuum Extraction & UV Sterilisers",
        "meta_tag": "Hypoallergenic Hygiene",
        "pills": [
            {"title": "Single / King Single", "desc": "1 Mattress"},
            {"title": "Double Mattress", "desc": "1 Double Bed"},
            {"title": "Queen Mattress", "desc": "Most Popular", "active": True},
            {"title": "King / Super King", "desc": "Master Suite"}
        ],
        "faqs": [
            ("Why should a mattress be professionally cleaned?", "A mattress traps millions of dead skin cells, perspiration, and microscopic dust mites that trigger asthma and eczema. Professional extraction restores true hygienic purity."),
            ("How soon can the bed be made and used?", "Carpets and mattresses are dry within 2 to 3 hours, meaning you can sleep on it the same night."),
            ("Can you remove urine stains and spill marks?", "We apply targeted bio-enzymatic agents that digest stain proteins and deodorise deep foam layers."),
            ("Is Urban Shield™ safe for allergy sufferers?", "Yes, it is dermatologically neutral and specifically formulated to eliminate allergens.")
        ]
    },
    {
        "slug": "floor-polishing-perth",
        "file": "floor-polishing-perth.md",
        "title_short": "Floor Refresh",
        "h1": "Timber Floor Refresh & High-Gloss Polishing",
        "meta_title": "Floor Polishing Perth | Timber Floor Refresh | Urban Shine",
        "meta_desc": "Professional timber floor polishing and refresh in Perth. Revive dull wood and polished concrete surfaces without the expense of full sanding.",
        "image": "assets/images/services/floor-polishing.png",
        "category": "floor",
        "badge": "Rapid Gloss Refresh • Low Cost",
        "turnaround": "2 – 4 Hours (Same-Day)",
        "equipment": "Rotary Floor Burnishers, Micro-Pads & Polish Applicators",
        "meta_tag": "Rapid Same-Day Gloss",
        "pills": [
            {"title": "1-2 Rooms (Up to 30m²)", "desc": "Entry / Dining"},
            {"title": "Medium Area (30–60m²)", "desc": "Living & Hallway", "active": True},
            {"title": "Large Area (60–100m²)", "desc": "Main Level"},
            {"title": "100m²+ Full House", "desc": "Complete Residence"}
        ],
        "faqs": [
            ("What is the difference between floor polishing and sanding?", "Polishing (or buff and coat) removes light scuffs and revitalises the existing topcoat without removing timber thickness. Sanding grinds the timber down to bare raw wood."),
            ("Can you polish engineered timber and laminate?", "We polish and buff solid timber, engineered wood, and decorative polished concrete. Laminates are treated with specialized gentle sealers."),
            ("How quickly can we walk on the floors?", "Our fast-curing coats allow light socks-only foot traffic within 4 to 6 hours.")
        ]
    },
    {
        "slug": "decking-restoration-perth",
        "file": "decking-restoration-perth.md",
        "title_short": "Decking",
        "h1": "Outdoor Decking Cleaning, Sanding & Oiling",
        "meta_title": "Decking Restoration Perth | Sanding, Oiling & Sealing | Urban Shine",
        "meta_desc": "Complete decking restoration in Perth. Weatherproofing, sanding, staining, and premium oil application to protect outdoor timber from harsh WA sun.",
        "image": "assets/images/services/decking-restoration.png",
        "category": "floor",
        "badge": "Weatherproof UV Protection",
        "turnaround": "1 – 2 Days",
        "equipment": "Heavy Deck Scrubbers, Rotary Sanders & Penetrating Oil Systems",
        "meta_tag": "Weatherproof UV Seal",
        "pills": [
            {"title": "Small Deck (<15m²)", "desc": "Courtyard / Patio"},
            {"title": "Medium Deck (15–30m²)", "desc": "Standard Verandah", "active": True},
            {"title": "Large Deck (30–55m²)", "desc": "Entertaining Deck"},
            {"title": "Multi-Level / 55m²+", "desc": "Pool Deck / Large Area"}
        ],
        "faqs": [
            ("How do you treat grey, sun-bleached timber?", "We deep-clean using timber rejuvenators to dissolve oxidised grey fibres, sand the surface silky smooth, and saturate the timber with UV-resistant oils."),
            ("What oils or stains do you use?", "We exclusively use premium Australian-formulated penetrating oils (such as Cutek or Feast Watson) designed specifically for severe Western Australian sun and moisture."),
            ("How often should a timber deck be re-oiled in Perth?", "Due to Perth's high UV index, outdoor decks exposed to direct sunlight benefit from a maintenance coat every 12 to 18 months.")
        ]
    },
    {
        "slug": "aircon-cleaning-perth",
        "file": "aircon-cleaning-perth.md",
        "title_short": "Aircon Cleaning",
        "h1": "Air Conditioning Deep Hydro-Clean & Flush",
        "meta_title": "Aircon Cleaning Perth | Hydro-Cleaning & Mould Flush | Urban Shine",
        "meta_desc": "Perth air conditioner hydro-cleaning and mould spore decontamination. Improves airflow, lowers electricity bills, and eradicates hidden indoor allergens.",
        "image": "assets/images/services/aircon-cleaning.jpg",
        "category": "cleaning",
        "badge": "Mould Spore Flush & Airflow Boost",
        "turnaround": "45 Mins per Split Unit",
        "equipment": "Enclosed Hydro Catchment Wash Bags & Fin Cleaners",
        "meta_tag": "Mould Spore Deep Flush",
        "pills": [
            {"title": "1 Split System Unit", "desc": "Standard Bedroom"},
            {"title": "2 Split System Units", "desc": "Living + Bed", "active": True},
            {"title": "3 Split System Units", "desc": "Full Apartment/House"},
            {"title": "4+ Units / Ducted Flush", "desc": "Multi-Zone System"}
        ],
        "faqs": [
            ("How does dirty air conditioning affect health?", "Aircon coils and blower wheels are dark, damp breeding grounds for black mould and bacteria. Every time you turn it on, spores circulate into your living room."),
            ("Does hydro-cleaning lower electricity consumption?", "Yes! When cooling fins and blower wheels are clear of packed dust, the compressor runs up to 30% more efficiently, lowering power bills."),
            ("Will water leak onto my walls or floor during cleaning?", "No. We mount waterproof catchment wash bags beneath the unit that drain all flushed waste into sealed containers.")
        ]
    },
    {
        "slug": "steam-cleaning-perth",
        "file": "steam-cleaning-perth.md",
        "title_short": "Steam Cleaning",
        "h1": "Chemical-Free High-Pressure Steam Cleaning",
        "meta_title": "Steam Cleaning Perth | Chemical-Free Sanitisation | Urban Shine",
        "meta_desc": "Superheated steam cleaning across Perth homes and businesses. Sanitise hard floors, kitchens, bathrooms, and high-touch areas without harsh chemicals.",
        "image": "assets/images/services/steam-cleaning.png",
        "category": "cleaning",
        "badge": "180°C Thermal Sanitisation",
        "turnaround": "1.5 – 3 Hours",
        "equipment": "Industrial Superheated Steam Boilers & Micro-Detail Brushes",
        "meta_tag": "180°C Thermal Hygiene",
        "pills": [
            {"title": "Kitchen & Bathrooms", "desc": "Tile & Sanitary Steam"},
            {"title": "Hard Floors & Living", "desc": "Up to 50m²", "active": True},
            {"title": "Full House Sanitisation", "desc": "Complete Deep Steam"},
            {"title": "Commercial Premises", "desc": "Offices & Retail"}
        ],
        "faqs": [
            ("How does chemical-free steam sanitize effectively?", "At temperatures exceeding 150°C, superheated dry vapor melts grease, destroys cell walls of bacteria, and eradicates 99.9% of microbial pathogens on contact."),
            ("Is this safe for pets and newborn babies?", "It is the safest cleaning method available because zero toxic chemicals, synthetic perfumes, or sticky residues remain."),
            ("Can steam clean hard-to-reach tracks and grout lines?", "Yes! High pressure narrow-nozzle attachments blast deep grime out of window tracks, door runners, and grout fissures.")
        ]
    },
    {
        "slug": "flood-damage-restoration-perth",
        "file": "flood-damage-restoration-perth.md",
        "title_short": "Flood Treatment",
        "h1": "24/7 Emergency Flood & Water Damage Restoration",
        "meta_title": "Flood Damage Restoration Perth | 24/7 Emergency | Urban Shine",
        "meta_desc": "24/7 emergency water extraction and structural drying in Perth. Prevent black mould, restore wet carpets and timber floors with rapid response.",
        "image": "assets/images/services/flood-damage.png",
        "category": "floor",
        "badge": "24/7 Rapid Emergency Response",
        "turnaround": "Immediate Dispatch (Within 60 Mins)",
        "equipment": "Submersible Heavy Extractors, LGR Dehumidifiers & Air Movers",
        "meta_tag": "24/7 Immediate Dispatch",
        "pills": [
            {"title": "Minor Pipe Leak", "desc": "1 Room / Damp Carpet"},
            {"title": "Burst Pipe / Sump Leak", "desc": "Multi-Room Extraction"},
            {"title": "Major Structural Flood", "desc": "Dehumidification Setup"},
            {"title": "Emergency Immediate Callout", "desc": "24/7 On-Call Team", "active": True}
        ],
        "faqs": [
            ("How quickly should water extraction begin?", "Within 24 to 48 hours is critical. After 48 hours, standing water fosters dangerous mould colonies and begins warping timber substrates."),
            ("Do you assist with insurance claims?", "Yes, we prepare detailed moisture mapping reports, equipment logs, and itemized scopes directly compliant with Australian home insurance requirements."),
            ("How do you ensure mould doesn't grow beneath the carpet?", "We lift carpet corners, extract underlay water, apply antimicrobial sanitiser (Urban Shield™), and position commercial LGR dehumidifiers and air movers until moisture meters read normal.")
        ]
    },
    {
        "slug": "floor-sanding-perth",
        "file": "floor-sanding-perth.md",
        "title_short": "Light Sanding",
        "h1": "Dust-Free Timber Floor Sanding",
        "meta_title": "Floor Sanding Perth | 99% Dust-Free Floor Sanding | Urban Shine",
        "meta_desc": "Perth's premier dust-free timber floor sanding service. Strips old yellowed varnish, scratches, and stains with 99% HEPA dust extraction.",
        "image": "assets/images/services/floor-sanding.jpg",
        "category": "floor",
        "badge": "99% HEPA Dust Extraction",
        "turnaround": "1 – 2 Days",
        "equipment": "Continuous Belt Sanders, Edgers & Rotary Dust Extractors",
        "meta_tag": "99% Dust-Free HEPA",
        "pills": [
            {"title": "Single Room", "desc": "Up to 20m²"},
            {"title": "2-3 Rooms (Up to 50m²)", "desc": "Living & Dining", "active": True},
            {"title": "Living Areas (50–85m²)", "desc": "Main Living Zone"},
            {"title": "Full Residence (85m²+)", "desc": "Whole House Restoration"}
        ],
        "faqs": [
            ("Is the floor sanding process really dust-free?", "Our machinery features advanced continuous cyclonic HEPA extraction units that capture 99% of airborne particles at the cutting head, keeping your furniture and walls clean."),
            ("Can you stain the floorboards a darker or lighter colour?", "Yes! Once sanded to bare wood, we can apply custom tinted stains—including walnut, Scandinavian blonde, and rich jarrah finishes."),
            ("What coatings do you apply over the sanded timber?", "We apply non-yellowing commercial polyurethane in matte, satin, or high-gloss sheens for decades of durability.")
        ]
    },
    {
        "slug": "floor-restoration-perth",
        "file": "floor-restoration-perth.md",
        "title_short": "Floor Restore",
        "h1": "Complete Timber Floor Restoration",
        "meta_title": "Floor Restoration Perth | Heritage & Commercial Wood | Urban Shine",
        "meta_desc": "Comprehensive timber floor restoration in Perth. Repair damaged floorboards, gouges, water marks, and historic timber with master craftsmanship.",
        "image": "assets/images/services/floor-restoration.png",
        "category": "floor",
        "badge": "Full Structural Leveling & Coating",
        "turnaround": "2 – 3 Days",
        "equipment": "Trio Multi-Disc Finishers, Board Clamps & Polyurethane Sealers",
        "meta_tag": "Full Structural Repair",
        "pills": [
            {"title": "Deep Scratch & Board Repair", "desc": "Targeted Section"},
            {"title": "Sand & Dual Polyurethane", "desc": "Medium Home Zone", "active": True},
            {"title": "Full Structural Restoration", "desc": "Severe Wear / Heritage"},
            {"title": "Commercial / Ballroom", "desc": "High Traffic Spec"}
        ],
        "faqs": [
            ("Can you replace individual broken or rotted floorboards?", "Yes, our master timber craftsmen source matching recycled or kiln-dried timber to stitch seamlessly into your existing floor pattern."),
            ("How do you fix cupped or warped boards?", "We assess moisture levels with digital probes, stabilize the substrate, and mechanically level the surface before fine sanding and sealing."),
            ("What warranty comes with full floor restoration?", "We offer an industry-leading multi-year adhesion guarantee alongside our 14-day satisfaction warranty.")
        ]
    },
    {
        "slug": "tile-and-grout-cleaning-perth",
        "file": "tile-and-grout-cleaning-perth.md",
        "title_short": "Tile & Grout",
        "h1": "Rotary Tile & Grout Deep Cleaning",
        "meta_title": "Tile and Grout Cleaning Perth | High-Pressure Rotary | Urban Shine",
        "meta_desc": "Restore gleaming tiles and spotless grout lines across Perth. High-pressure rotary extraction lifts embedded dirt and grease from ceramic, porcelain, and stone.",
        "image": "assets/images/services/tile-and-grout.jpg",
        "category": "cleaning",
        "badge": "Rotary Pressure Extraction",
        "turnaround": "1 – 3 Hours",
        "equipment": "Rotary Enclosed Extraction Hydro-Heads (1000 PSI)",
        "meta_tag": "1000 PSI Rotary Clean",
        "pills": [
            {"title": "Up to 25m²", "desc": "Kitchen or 2 Baths"},
            {"title": "25m² – 50m²", "desc": "Kitchen + Living", "active": True},
            {"title": "50m² – 80m²", "desc": "Main Living Areas"},
            {"title": "80m²+ Whole Home", "desc": "Full Interior Tiles"}
        ],
        "faqs": [
            ("Why doesn't regular mopping clean grout lines?", "Mops push dirty wash water directly into porous grout lines where grime settles and darkens. Our rotary tool injects 1000 PSI water and immediately vacuums it away."),
            ("Do you offer grout sealing after cleaning?", "Yes, we can apply an impenetrable clear barrier seal that stops spills from soaking into the grout pores in the future."),
            ("Can you clean porous stone like travertine or slate?", "Absolutely. We calibrate pressure and select neutral chemistry specifically for natural stone.")
        ]
    }
]

def get_header(current_page=""):
    return f'''
  <!-- Top Utility Bar (UrbanX Design) -->
  <aside class="utility-bar" aria-label="Quick Contact and Hours">
    <div class="container utility-container">
      <div class="util-left">
        <span>Cleaning & Floor Restoration • Residential & Commercial Services</span>
      </div>
      <div class="util-right">
        <a href="mailto:info@urbanshinemelb.com.au" class="util-link">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
          <span>info@urbanshinemelb.com.au</span>
        </a>
        <a href="tel:+61432979551" class="util-link">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          <span>+61 432 979 551</span>
        </a>
        <a href="contact-urban-shine-perth.html#service-areas" class="util-link">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
          <span>Perth Service Areas</span>
        </a>
      </div>
    </div>
  </aside>

  <!-- Main Sticky Header -->
  <header class="main-header" role="banner">
    <div class="container header-container">
      <a href="index.html" class="brand-logo" aria-label="Urban Shine Homepage">
        <img src="assets/images/logo-emblem.png" alt="Urban Shine Emblem" class="brand-emblem-img" style="height: 46px; width: auto; object-fit: contain;">
        <div class="brand-text-block">
          <div class="brand-title">URBAN<span>SHINE</span></div>
          <div class="brand-subtitle">HOME SERVICE</div>
        </div>
      </a>

      <nav class="primary-nav" aria-label="Main navigation">
        <div class="nav-item">
          <span class="nav-link">
            Cleaning Services
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </span>
          <div class="nav-dropdown">
            <a href="carpet-cleaning-perth.html" class="dropdown-link"><span>Carpet Steam Cleaning</span><span>→</span></a>
            <a href="couch-cleaning-perth.html" class="dropdown-link"><span>Couch & Upholstery Care</span><span>→</span></a>
            <a href="curtain-cleaning-perth.html" class="dropdown-link"><span>On-Site Curtain Cleaning</span><span>→</span></a>
            <a href="mattress-cleaning-perth.html" class="dropdown-link"><span>Mattress Sanitisation</span><span>→</span></a>
            <a href="steam-cleaning-perth.html" class="dropdown-link"><span>Chemical-Free Steam Clean</span><span>→</span></a>
            <a href="tile-and-grout-cleaning-perth.html" class="dropdown-link"><span>Tile & Grout Deep Clean</span><span>→</span></a>
            <a href="aircon-cleaning-perth.html" class="dropdown-link"><span>Aircon Hydro-Cleaning</span><span>→</span></a>
          </div>
        </div>

        <div class="nav-item">
          <span class="nav-link">
            Floor & Outdoor
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </span>
          <div class="nav-dropdown">
            <a href="floor-sanding-perth.html" class="dropdown-link"><span>Dust-Free Floor Sanding</span><span>→</span></a>
            <a href="floor-polishing-perth.html" class="dropdown-link"><span>Floor Refresh & Polish</span><span>→</span></a>
            <a href="floor-restoration-perth.html" class="dropdown-link"><span>Complete Floor Restoration</span><span>→</span></a>
            <a href="decking-restoration-perth.html" class="dropdown-link"><span>Outdoor Decking Restoration</span><span>→</span></a>
            <a href="flood-damage-restoration-perth.html" class="dropdown-link"><span>Flood & Water Restoration</span><span>→</span></a>
          </div>
        </div>

        <a href="professional-cleaning-services-perth.html" class="nav-link {'active' if current_page=='services' else ''}">All Services</a>
        <a href="about.html" class="nav-link {'active' if current_page=='about' else ''}">About Us</a>
        <a href="contact-urban-shine-perth.html" class="nav-link {'active' if current_page=='contact' else ''}">Contact</a>
      </nav>

      <div style="display: flex; align-items: center; gap: 14px;">
        <a href="tel:+61432979551" class="btn btn-outline btn-sm header-phone-btn" style="display: inline-flex; align-items: center; gap: 6px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          <span>0432 979 551</span>
        </a>
        <a href="book.html" class="btn btn-primary btn-sm">
          Book Assessment
        </a>
        <button class="mobile-toggle" aria-label="Toggle Navigation">
          ☰
        </button>
      </div>
    </div>
  </header>
'''

def get_footer():
    return '''
  <!-- ==========================================================================
       Footer (Exact Home Page 4-Column Directory Architecture)
       ========================================================================== -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <!-- Col 1: Brand -->
        <div class="footer-brand">
          <a href="index.html" class="brand-logo" style="margin-bottom: 16px;">
            <img src="assets/images/logo-emblem.png" alt="Urban Shine Emblem" class="brand-emblem-img" style="height: 44px; width: auto; object-fit: contain;">
            <div class="brand-text-block">
              <div class="brand-title" style="color: #FFFFFF;">URBAN<span style="color:var(--color-accent);">SHINE</span></div>
              <div class="brand-subtitle" style="color: #94A3B8;">HOME SERVICE</div>
            </div>
          </a>
          <p>
            At Urban Shine, we provide professional cleaning and restorative floor management for residential and commercial properties across Perth.
          </p>
          <div class="footer-contact-list">
            <div class="footer-contact-item">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              <span>Dispatch: <a href="tel:+61432979551" style="color:#FFFFFF; font-weight:600;">+61 432 979 551</a></span>
            </div>
            <div class="footer-contact-item">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <span>info@urbanshinemelb.com.au</span>
            </div>
            <div class="footer-contact-item">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span>Perth, WA — Mobile Dispatch by Appointment</span>
            </div>
          </div>
        </div>

        <!-- Col 2: Cleaning Services -->
        <div>
          <h4 class="footer-title">Cleaning Services</h4>
          <div class="footer-links">
            <a href="carpet-cleaning-perth.html" class="footer-link">Carpet Steam Cleaning</a>
            <a href="couch-cleaning-perth.html" class="footer-link">Couch & Sofa Care</a>
            <a href="curtain-cleaning-perth.html" class="footer-link">On-Site Curtain Clean</a>
            <a href="mattress-cleaning-perth.html" class="footer-link">Mattress Sanitisation</a>
            <a href="steam-cleaning-perth.html" class="footer-link">Chemical-Free Steam</a>
            <a href="aircon-cleaning-perth.html" class="footer-link">Aircon Split Flush</a>
          </div>
        </div>

        <!-- Col 3: Floor & Timber Care -->
        <div>
          <h4 class="footer-title">Floor & Timber Care</h4>
          <div class="footer-links">
            <a href="floor-polishing-perth.html" class="footer-link">Floor Refresh & Polish</a>
            <a href="floor-sanding-perth.html" class="footer-link">Dust-Free Floor Sanding</a>
            <a href="floor-restoration-perth.html" class="footer-link">Complete Restoration</a>
            <a href="tile-and-grout-cleaning-perth.html" class="footer-link">Tile & Grout Deep Clean</a>
            <a href="decking-restoration-perth.html" class="footer-link">Outdoor Decking</a>
            <a href="flood-damage-restoration-perth.html" class="footer-link">24/7 Flood Response</a>
          </div>
        </div>

        <!-- Col 4: Newsletter / Dispatch -->
        <div class="footer-newsletter">
          <h4 class="footer-title">Urban Shine Dispatch</h4>
          <p>Sign up to receive updates about our services, promotions and cleaning tips!</p>
          <form class="footer-form" onsubmit="event.preventDefault(); alert('Subscribed to Urban Shine updates!'); this.reset();">
            <input type="email" class="footer-input" placeholder="Enter your email..." required>
            <button type="submit" class="btn btn-primary btn-sm">Join</button>
          </form>
          <div style="margin-top: 18px; font-size: 0.8125rem; color: #34D399; display: flex; align-items: center; gap: 6px;">
            <span>🛡️ Operating under WA quality standards</span>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          © 2026 Urban Shine. Professional cleaning services across Perth, Western Australia.
        </div>
        <div style="display: flex; gap: 20px;">
          <a href="about.html" class="footer-link">About Us</a>
          <a href="contact-urban-shine-perth.html" class="footer-link">Contact</a>
          <a href="book.html" class="footer-link">Book Assessment</a>
          <a href="about.html#guarantee" class="footer-link">14-Day Guarantee</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Floating Dispatch Pill -->
  <a href="tel:+61432979551" class="floating-dispatch" aria-label="Call Perth Cleaning Dispatch">
    <span>Perth Cleaning Dispatch • Call Now</span>
    <div class="dispatch-circle">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
    </div>
  </a>
'''

def parse_service_markdown(file_name):
    path = os.path.join(CONTEXT_DIR, file_name)
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    body_part = raw.split("## Full Content Text")[1].split("## Images")[0]
    lines = [l.strip() for l in body_part.split("\n") if l.strip()]

    # Extract features
    features = []
    i = 0
    while i < len(lines) and len(features) < 6:
        if lines[i] == '✔' and i + 2 < len(lines):
            features.append((lines[i+1], lines[i+2]))
            i += 3
        else:
            i += 1

    # Extract About Us block
    about_idx = -1
    for idx, l in enumerate(lines):
        if l.upper() == 'ABOUT US':
            about_idx = idx
            break

    # Find where pillars start
    sq_idx = -1
    for idx, l in enumerate(lines):
        if l in ['Service Quality', 'Modern Tech', 'Modern Technology']:
            sq_idx = idx
            break

    about_heading = "Trusted Cleaning Specialists Perth Homeowners Rely On"
    about_paragraphs = []
    if about_idx != -1:
        if about_idx + 1 < len(lines):
            about_heading = lines[about_idx + 1]
        end_p = sq_idx if sq_idx != -1 else len(lines)
        about_paragraphs = lines[about_idx + 2:end_p]

    return {
        "features": features,
        "about_heading": about_heading,
        "about_paragraphs": about_paragraphs
    }

def generate_service_page(meta):
    slug = meta["slug"]
    data = parse_service_markdown(meta["file"])
    title = meta["h1"]
    meta_title = meta["meta_title"]
    meta_desc = meta["meta_desc"]
    image = meta["image"]
    badge = meta["badge"]
    turnaround = meta["turnaround"]
    equipment = meta["equipment"]
    pills = meta["pills"]
    faqs = meta["faqs"]

    # Render Pills HTML (No Prices)
    pills_html = ""
    for idx, p in enumerate(pills):
        active_cls = "active" if p.get("active") else ""
        checked_attr = "checked" if p.get("active") else ""
        pills_html += f'''
          <label class="scope-pill {active_cls}">
            <input type="radio" name="service_scope" value="{p['title']}" {checked_attr}>
            <span class="scope-pill-title">{p['title']}</span>
            <span class="scope-pill-desc">{p['desc']}</span>
          </label>
        '''

    # Render Features HTML
    features_html = ""
    for f_title, f_desc in data["features"]:
        features_html += f'''
          <div class="checklist-item">
            <h4><span class="check">✔</span> {f_title}</h4>
            <p>{f_desc}</p>
          </div>
        '''

    # Render About Paragraphs
    about_paras_html = ""
    for p in data["about_paragraphs"]:
        about_paras_html += f"<p>{p}</p>\n"

    # Render FAQs HTML
    faqs_html = ""
    for q, a in faqs:
        faqs_html += f'''
          <div class="faq-item">
            <button class="faq-header" type="button">
              <span class="faq-question">{q}</span>
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-body">
              <div class="faq-answer">{a}</div>
            </div>
          </div>
        '''

    html_content = f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{meta_title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="icon" type="image/png" href="assets/images/logo-emblem.png">
  
  <meta property="og:type" content="website">
  <meta property="og:title" content="{meta_title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="https://urbanshinemelb.com.au/{slug}.html">
  
  <link rel="stylesheet" href="css/style.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "{title}",
    "provider": {{
      "@type": "HomeAndConstructionBusiness",
      "name": "Urban Shine",
      "telephone": "+61432979551",
      "email": "info@urbanshinemelb.com.au",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Perth",
        "addressRegion": "WA",
        "addressCountry": "AU"
      }}
    }},
    "areaServed": "Perth Western Australia",
    "description": "{meta_desc}"
  }}
  </script>
</head>
<body>

{get_header(current_page="services")}

  <!-- Service Subpage Hero -->
  <section class="page-hero" style="background: linear-gradient(90deg, rgba(8, 11, 44, 0.96) 0%, rgba(8, 11, 44, 0.88) 55%, rgba(8, 11, 44, 0.45) 100%), url('{image}') center/cover no-repeat;">
    <div class="page-hero-pattern"></div>
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="separator">/</span>
        <a href="professional-cleaning-services-perth.html">Services</a>
        <span class="separator">/</span>
        <span class="current">{title}</span>
      </nav>

      <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(247,134,20,0.15); border:1px solid rgba(247,134,20,0.35); padding:6px 14px; border-radius:9999px; margin-bottom:16px;">
        <span style="color:var(--color-accent-light); font-weight:700; font-size:0.75rem; letter-spacing:0.06em; text-transform:uppercase;">
          {badge}
        </span>
      </div>

      <h1>{title} Across <span style="color:var(--color-accent-light);">Perth</span></h1>
      
      <p class="page-hero-desc">
        Engineered for precision results. We combine industrial-grade equipment, fiber-safe pH chemistry, and our complimentary Urban Shield™ 99.9% antibacterial barrier to restore your space with a 14-day re-treatment guarantee.
      </p>

      <!-- Trust Strip -->
      <div style="display:flex; flex-wrap:wrap; gap:20px; align-items:center; font-size:0.875rem; color:var(--color-gray-300); margin-top:24px;">
        <div style="display:flex; align-items:center; gap:6px;">
          <span style="color:#F59E0B;">★★★★★</span>
          <strong>4.7/5 Feefo Verified</strong>
        </div>
        <span style="color:var(--color-gray-600);">•</span>
        <div style="display:flex; align-items:center; gap:6px;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          <span>Licensed WA Technicians</span>
        </div>
        <span style="color:var(--color-gray-600);">•</span>
        <div style="display:flex; align-items:center; gap:6px;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          <span>14-Day Free Re-Treatment</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Main 2-Column Content Section -->
  <main class="section section-alt" style="padding: 48px 0 80px 0;">
    <div class="container">
      <div class="content-grid-sidebar">
        
        <!-- Left 2/3 Content Column -->
        <article class="main-column">
          
          <!-- Compliance Strip -->
          <div class="compliance-strip" style="margin-top:0;">
            <div class="compliance-info">
              <div class="compliance-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><polyline points="9 12 11 14 15 10"></polyline></svg>
              </div>
              <div class="compliance-text">
                <strong>Western Australian Cleaning & Chemical Safety Compliant</strong>
                <p>Delivered by police-checked, insured technicians using hospital-grade sanitisation and zero harmful volatile compounds.</p>
              </div>
            </div>
          </div>

          <!-- Section 1: Why Choose Urban Shine -->
          <div class="content-block">
            <h2>Why Choose Urban Shine for {title} Perth</h2>
            <p>Our systematic methodology ensures deep restorative cleaning, maximum hygiene, and zero risk of material damage.</p>
            <div class="feature-checklist-grid">
              {features_html}
            </div>
          </div>

          <!-- Section 2: Authentic In-Depth Service Overview & Context -->
          <div class="content-block">
            <h2>{data["about_heading"]}</h2>
            {about_paras_html}
          </div>

          <!-- Section 3: Visual Showcase & Field Operations -->
          <div class="content-block">
            <h2>Field Operations & Equipment Showcase</h2>
            <p style="margin-bottom:20px;">Every clean is executed with industrial equipment tailored specifically to the textile or substrate type:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:24px; align-items:center;">
              <div style="border-radius:var(--radius-md); overflow:hidden; border:1px solid var(--color-gray-200); box-shadow:var(--shadow-sm); max-height:360px;">
                <img src="{image}" alt="{title} in Action" style="width:100%; height:100%; object-fit:cover; display:block;">
              </div>
              <div>
                <h4 style="font-size:1.125rem; font-weight:700; color:var(--color-navy); margin-bottom:8px;">Specialized Equipment Spec</h4>
                <p style="font-size:0.9375rem; color:var(--color-gray-600); margin-bottom:14px;"><strong>Machinery:</strong> {equipment}</p>
                <p style="font-size:0.9375rem; color:var(--color-gray-600); margin-bottom:14px;"><strong>Turnaround:</strong> {turnaround}</p>
                <p style="font-size:0.9375rem; color:var(--color-gray-600); margin-bottom:16px;"><strong>Protection Layer:</strong> Complimentary hospital-grade Urban Shield™ antimicrobial barrier applied post-clean.</p>
                <a href="book.html?service={slug}" class="btn btn-primary btn-sm">Request Free Assessment</a>
              </div>
            </div>
          </div>

          <!-- Section 4: 3 Pillars of Excellence -->
          <div class="content-block">
            <h2>Our Operational Standards & Modern Equipment</h2>
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:16px; margin-top:20px;">
              <div style="background:var(--color-gray-50); border:1px solid var(--color-gray-200); padding:20px; border-radius:var(--radius-md);">
                <div style="font-size:1.5rem; margin-bottom:8px;">🏆</div>
                <h4 style="font-size:1rem; font-weight:700; color:var(--color-navy); margin-bottom:6px;">Service Quality</h4>
                <p style="font-size:0.8125rem; color:var(--color-gray-600); line-height:1.5; margin:0;">Improves indoor air quality, eliminates deep allergens, and revitalises surface appearance on every visit.</p>
              </div>
              <div style="background:var(--color-gray-50); border:1px solid var(--color-gray-200); padding:20px; border-radius:var(--radius-md);">
                <div style="font-size:1.5rem; margin-bottom:8px;">⚙️</div>
                <h4 style="font-size:1rem; font-weight:700; color:var(--color-navy); margin-bottom:6px;">Modern Tech</h4>
                <p style="font-size:0.8125rem; color:var(--color-gray-600); line-height:1.5; margin:0;">Utilising {equipment} that lifts soil without oversaturating or damaging fibers.</p>
              </div>
              <div style="background:var(--color-gray-50); border:1px solid var(--color-gray-200); padding:20px; border-radius:var(--radius-md);">
                <div style="font-size:1.5rem; margin-bottom:8px;">👨‍🔧</div>
                <h4 style="font-size:1rem; font-weight:700; color:var(--color-navy); margin-bottom:6px;">Expert Team</h4>
                <p style="font-size:0.8125rem; color:var(--color-gray-600); line-height:1.5; margin:0;">Trained technicians certified to safely handle fine fabrics, delicate wools, and prestige hardwood.</p>
              </div>
            </div>
          </div>

          <!-- Section 5: 5-Step Process Timeline -->
          <div class="content-block">
            <h2>The Urban Shine 5-Step Precision Workflow</h2>
            <p>We execute every treatment with structured rigor to achieve spotless, hygienic, and long-lasting outcomes.</p>
            <div class="process-timeline">
              <div class="process-step-card">
                <div class="step-number-badge">01</div>
                <div class="step-details">
                  <h4>Pre-Inspection & Material Diagnostics</h4>
                  <p>We inspect fibers, test pH tolerance, identify spot origins, and check join stability before touching any surface.</p>
                </div>
              </div>
              <div class="process-step-card">
                <div class="step-number-badge">02</div>
                <div class="step-details">
                  <h4>Targeted Soil Pre-Treatment</h4>
                  <p>Eco-friendly emulsifiers penetrate deep into the material to break down stubborn grease, stains, and trapped dirt.</p>
                </div>
              </div>
              <div class="process-step-card">
                <div class="step-number-badge">03</div>
                <div class="step-details">
                  <h4>High-Power Extraction & Thermal Rinse</h4>
                  <p>Our equipment flushes away suspended grime with calibrated hot water, simultaneously vacuuming away 95% of moisture.</p>
                </div>
              </div>
              <div class="process-step-card">
                <div class="step-number-badge">04</div>
                <div class="step-details">
                  <h4>Free Urban Shield™ 99.9% Application</h4>
                  <p>We apply our proprietary antimicrobial formulation to kill bacteria, banish odours, and protect against rapid re-soiling.</p>
                </div>
              </div>
              <div class="process-step-card">
                <div class="step-number-badge">05</div>
                <div class="step-details">
                  <h4>Final Pile Grooming & Client Walkthrough</h4>
                  <p>We groom fibers for rapid air circulation, inspect every inch under high-intensity lamps, and review with you.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Section 6: Verified Customer Reviews -->
          <div class="content-block">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; flex-wrap:wrap; gap:12px;">
              <div>
                <h2>Verified Customer Reviews</h2>
                <p style="margin:0; font-size:0.875rem; color:var(--color-gray-500);">Independent Service Rating based on verified Perth homeowners</p>
              </div>
              <div style="background:var(--color-gray-50); border:1px solid var(--color-gray-200); padding:8px 16px; border-radius:var(--radius-sm); display:flex; align-items:center; gap:8px;">
                <span style="font-weight:800; font-size:1.25rem; color:var(--color-navy);">4.7 / 5.0</span>
                <span style="color:#F59E0B; font-size:1.1rem;">★★★★★</span>
              </div>
            </div>

            <div class="reviews-grid" style="grid-template-columns:1fr 1fr;">
              <div class="review-card">
                <div>
                  <div class="review-stars">★★★★★</div>
                  <h4 class="review-title">Excellent Job</h4>
                  <p class="review-text">Prompt, clean, professional. My carpets look brand new and dried in just a couple of hours. Very impressed!</p>
                </div>
                <div class="review-author">
                  <div class="review-avatar">DM</div>
                  <div>
                    <h5>Denise Mclennan</h5>
                    <p>Verified Homeowner</p>
                  </div>
                </div>
              </div>
              <div class="review-card">
                <div>
                  <div class="review-stars">★★★★★</div>
                  <h4 class="review-title">Fast & Efficient</h4>
                  <p class="review-text">The technician arrived right on schedule, treated stubborn high-traffic stains and applied Urban Shield. Outstanding service!</p>
                </div>
                <div class="review-author">
                  <div class="review-avatar">PR</div>
                  <div>
                    <h5>Peter Richardson</h5>
                    <p>Verified Homeowner</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Section 7: 14-Day Guarantee Card -->
          <div style="background:linear-gradient(135deg, #FFF7ED 0%, #FFF3E5 100%); border:2px solid var(--color-accent-border); border-radius:var(--radius-lg); padding:32px; display:flex; gap:20px; align-items:center;">
            <div style="width:60px; height:60px; border-radius:50%; background:var(--color-accent); color:#FFF; display:flex; align-items:center; justify-content:center; flex-shrink:0; font-size:1.75rem;">
              🛡️
            </div>
            <div>
              <h3 style="font-family:var(--font-display); font-size:1.25rem; font-weight:700; color:var(--color-navy); margin-bottom:6px;">
                The Urban Shine 14-Day Peace of Mind Guarantee
              </h3>
              <p style="font-size:0.9375rem; color:var(--color-gray-700); line-height:1.6; margin:0;">
                Our 14-day satisfaction guarantee ensures total peace of mind. If you notice any area that requires additional attention after drying, our technicians will return promptly and re-treat the area completely free of charge.
              </p>
            </div>
          </div>

          <!-- Section 8: FAQs -->
          <div class="content-block">
            <h2>Frequently Asked Questions</h2>
            <div class="faq-accordion">
              {faqs_html}
            </div>
          </div>

        </article>

        <!-- Right 1/3 Sticky Sidebar Form (No Hardcoded Price Numbers) -->
        <aside class="sticky-sidebar">
          
          <div class="sidebar-form-card">
            <h3 class="sidebar-form-title">Request Assessment & Dispatch</h3>
            <p class="sidebar-form-subtitle">Perth Metro • Free Urban Shield™ Included</p>

            <div class="sidebar-price-estimate">
              <div class="sidebar-price-label">Service Scope & Assessment</div>
              <div class="sidebar-price-amount" style="font-size: 1.375rem; font-weight: 800; color: #FFFFFF;">
                Free On-Site Assessment
              </div>
              <div class="sidebar-price-sub">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Includes Free Urban Shield™ 99.9%</span>
              </div>
            </div>

            <!-- The Form -->
            <form class="sidebar-quote-form" data-service-title="{title}">
              <div class="form-group">
                <label class="form-label">Select Treatment Scope</label>
                <div class="scope-pills">
                  {pills_html}
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="quoteDate_{slug}">Preferred Service Date</label>
                <input type="date" id="quoteDate_{slug}" name="service_date" class="form-control">
              </div>

              <div class="form-group">
                <label class="form-label" for="quoteName_{slug}">Full Name *</label>
                <input type="text" id="quoteName_{slug}" name="client_name" class="form-control" placeholder="e.g. Sarah Jenkins" required>
              </div>

              <div class="form-group">
                <label class="form-label" for="quotePhone_{slug}">Mobile Phone *</label>
                <input type="tel" id="quotePhone_{slug}" name="client_phone" class="form-control" placeholder="04XX XXX XXX" required>
              </div>

              <div class="form-group">
                <label class="form-label" for="quoteSuburb_{slug}">Perth Suburb or Postcode *</label>
                <input type="text" id="quoteSuburb_{slug}" name="client_suburb" class="form-control" placeholder="e.g. Cottesloe, Dalkeith, 6000" required>
              </div>

              <button type="submit" class="btn btn-primary" style="width: 100%; padding: 14px; font-weight: 700; margin-top: 8px;">
                Lock In Assessment & Dispatch →
              </button>
            </form>

            <div style="text-align: center; margin-top: 14px; font-size: 0.75rem; color: var(--color-gray-500);">
              🔒 Backed by 14-Day Free Re-Treatment Guarantee
            </div>
          </div>

          <!-- Quick Help Card -->
          <div class="sidebar-help-card">
            <h4>Direct Perth Booking Support</h4>
            <p>Speak directly with a Master Cleaner to discuss heavy stains or urgent callouts:</p>
            <a href="tel:+61432979551" class="sidebar-help-phone">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              <span>0432 979 551</span>
            </a>
            <div class="sidebar-help-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              <span>24/7 Operations & Emergency Ready</span>
            </div>
            <div class="sidebar-help-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              <span>Fully Insured Up to $20,000,000</span>
            </div>
          </div>

        </aside>
      </div>
    </div>
  </main>

{get_footer()}

  <script src="js/app.js"></script>
</body>
</html>'''

    output_path = os.path.join(SITE_DIR, f"{slug}.html")
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(html_content)
    print(f"Generated: {slug}.html")

def generate_services_directory_page():
    cards_html = ""
    for meta in SERVICES_META:
        slug = meta["slug"]
        title_short = meta.get("title_short", meta["h1"])
        h1 = meta["h1"]
        desc = meta["meta_desc"]
        img = meta["image"]
        badge = meta["badge"]
        turnaround = meta["turnaround"]
        category = meta["category"]
        meta_tag = meta.get("meta_tag", "Free Urban Shield™")

        cards_html += f'''
          <div class="service-photo-card service-directory-card" data-category="{category}">
            <!-- Top Navy Header Banner (Original Style) -->
            <div class="service-photo-header">
              <h3>{title_short}</h3>
            </div>
            
            <!-- Authentic Technician Photo -->
            <div class="service-photo-media">
              <img src="{img}" alt="{h1} Perth" loading="lazy">
              <div class="service-photo-overlay-badge">{badge}</div>
            </div>

            <!-- Card Content Body -->
            <div class="service-photo-body">
              <p class="service-photo-desc">{desc}</p>
              
              <div class="service-photo-meta">
                <span>⏱️ {turnaround}</span>
                <span class="service-meta-badge">✓ {meta_tag}</span>
              </div>

              <div class="service-photo-actions">
                <a href="{slug}.html" class="service-learn-btn">
                  LEARN MORE
                </a>
                <a href="book.html?service={slug}" class="service-book-btn">
                  BOOK NOW
                </a>
              </div>
            </div>
          </div>
        '''

    content = f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Professional Cleaning & Floor Care Services Perth | Urban Shine</title>
  <meta name="description" content="Explore Urban Shine's comprehensive cleaning and floor restoration services in Perth: carpet steam cleaning, couches, curtains, mattresses, timber sanding & flood care.">
  <link rel="icon" type="image/png" href="assets/images/logo-emblem.png">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

{get_header(current_page="services")}

  <section class="page-hero" style="background: linear-gradient(90deg, rgba(8, 11, 44, 0.96) 0%, rgba(8, 11, 44, 0.88) 55%, rgba(8, 11, 44, 0.45) 100%), url('assets/images/services/carpet-cleaning.png') center/cover no-repeat;">
    <div class="page-hero-pattern"></div>
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="separator">/</span>
        <span class="current">Our Services</span>
      </nav>

      <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(247,134,20,0.15); border:1px solid rgba(247,134,20,0.35); padding:6px 14px; border-radius:9999px; margin-bottom:16px;">
        <span style="color:var(--color-accent-light); font-weight:700; font-size:0.75rem; letter-spacing:0.06em; text-transform:uppercase;">
          12 SPECIALISED CLEANING & RESTORATION DISCIPLINES
        </span>
      </div>

      <h1>Professional Cleaning & Floor Care <span style="color:var(--color-accent-light);">Perth</span></h1>
      <p class="page-hero-desc">
        From deep hot water extraction and hospital-grade sanitisation to precision dust-free timber floor sanding and emergency flood remediation. All services include our 14-day re-treatment guarantee.
      </p>
    </div>
  </section>

  <main class="section section-alt" style="padding: 48px 0 80px 0;">
    <div class="container">

      <!-- Category Filter Tabs -->
      <div class="services-tabs">
        <button class="tab-btn active" data-tab="all">All Services (12)</button>
        <button class="tab-btn" data-tab="cleaning">Interior Cleaning (7)</button>
        <button class="tab-btn" data-tab="floor">Floors & Outdoor (5)</button>
      </div>

      <!-- Services Grid (Photo Cards without Prices) -->
      <div class="services-grid" style="grid-template-columns: repeat(3, 1fr); gap: 28px;">
        {cards_html}
      </div>

      <!-- Values Callout -->
      <div class="content-block" style="margin-top:64px;">
        <div style="text-align:center; max-width:700px; margin:0 auto 36px auto;">
          <div class="section-label">THE URBAN SHINE STANDARD</div>
          <h2 style="font-size:2rem;">Our Core Operating Values</h2>
          <p style="color:var(--color-gray-600);">Every service we deliver is anchored in our four non-negotiable commitments to Western Australian property owners.</p>
        </div>
        <div class="values-grid">
          <div class="value-card">
            <h4>A Can-Do Attitude</h4>
            <p>Our team takes a positive and problem-solving approach to every job, committed to achieving the cleanest possible outcome regardless of initial staining or wear.</p>
          </div>
          <div class="value-card">
            <h4>Keeping It Authentic</h4>
            <p>Empathetic, respectful, and upfront with transparent pricing. We inspect and test fibers accurately before making commitments.</p>
          </div>
          <div class="value-card">
            <h4>Customer-First</h4>
            <p>We work around your schedule, provide fast drying techniques to minimize home downtime, and treat your furnishings with genuine care.</p>
          </div>
          <div class="value-card">
            <h4>Focus On Quality</h4>
            <p>Hospital-grade sanitisation, continuous dust-extraction technology, and our unconditional 14-day free re-treatment guarantee.</p>
          </div>
        </div>
      </div>

    </div>
  </main>

{get_footer()}

  <script src="js/app.js"></script>
</body>
</html>'''
    with open(os.path.join(SITE_DIR, "professional-cleaning-services-perth.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated: professional-cleaning-services-perth.html")

def update_index_page():
    with open(os.path.join(SITE_DIR, "index.html"), "r", encoding="utf-8") as f:
        idx = f.read()

    # 1. Update Favicon in head
    if '<link rel="icon"' not in idx:
        idx = idx.replace('</title>', '</title>\n  <link rel="icon" type="image/png" href="assets/images/logo-emblem.png">')
    else:
        idx = re.sub(r'<link rel="icon"[^>]*>', '<link rel="icon" type="image/png" href="assets/images/logo-emblem.png">', idx)

    # 2. Update Header Brand Logo
    header_logo_pattern = re.compile(r'<a href="[^"]*" class="brand-logo" aria-label="Urban Shine Homepage">.*?</a>', re.DOTALL)
    new_header_logo = '''<a href="index.html" class="brand-logo" aria-label="Urban Shine Homepage">
        <img src="assets/images/logo-emblem.png" alt="Urban Shine Emblem" class="brand-emblem-img" style="height: 46px; width: auto; object-fit: contain;">
        <div class="brand-text-block">
          <div class="brand-title">URBAN<span>SHINE</span></div>
          <div class="brand-subtitle">HOME SERVICE</div>
        </div>
      </a>'''
    idx = header_logo_pattern.sub(new_header_logo, idx, count=1)

    # 3. Generate 12 photo cards without prices
    cards_html = ""
    for meta in SERVICES_META:
        slug = meta["slug"]
        title_short = meta.get("title_short", meta["h1"])
        h1 = meta["h1"]
        desc = meta["meta_desc"]
        img = meta["image"]
        badge = meta["badge"]
        turnaround = meta["turnaround"]
        category = meta["category"]
        meta_tag = meta.get("meta_tag", "Free Urban Shield™")

        cards_html += f'''
        <!-- {title_short} Photo Card -->
        <div class="service-photo-card" data-category="{category}">
          <div class="service-photo-header">
            <h3>{title_short}</h3>
          </div>
          <div class="service-photo-media">
            <img src="{img}" alt="{h1} Perth" loading="lazy">
            <div class="service-photo-overlay-badge">{badge}</div>
          </div>
          <div class="service-photo-body">
            <p class="service-photo-desc">{desc}</p>
            <div class="service-photo-meta">
              <span>⏱️ {turnaround}</span>
              <span class="service-meta-badge">✓ {meta_tag}</span>
            </div>
            <div class="service-photo-actions">
              <a href="{slug}.html" class="service-learn-btn">
                LEARN MORE
              </a>
              <a href="book.html?service={slug}" class="service-book-btn">
                BOOK NOW
              </a>
            </div>
          </div>
        </div>
'''

    # Replace services grid in index.html
    grid_pattern = re.compile(r'<div class="services-grid">.*?</div>\s*<!-- \/Services Grid -->', re.DOTALL)
    if grid_pattern.search(idx):
        idx = grid_pattern.sub(f'<div class="services-grid">\n{cards_html}      </div>\n      <!-- /Services Grid -->', idx)
    else:
        # manual slice
        g_start = idx.find('<div class="services-grid">')
        g_end = idx.find('<!-- View All Services CTA -->')
        if g_start != -1 and g_end != -1:
            idx = idx[:g_start] + f'<div class="services-grid">\n{cards_html}      </div>\n\n      ' + idx[g_end:]

    # 4. Remove Upfront Pricing Calculator section (#calculator)
    calc_pattern = re.compile(r'<!-- =+\s*Instant Price & Cost Estimator Calculator.*?<!-- =+\s*Why Choose Urban Shine', re.DOTALL)
    idx = calc_pattern.sub('<!-- ==========================================================================\n       Why Choose Urban Shine', idx)

    # 5. Remove "Clear Upfront Pricing" card (Image 5)
    upfront_card_pattern = re.compile(r'<div class="why-card">\s*<div class="why-icon">.*?<h3 class="why-title">Clear Upfront Pricing</h3>.*?</div>\s*</div>', re.DOTALL)
    idx = upfront_card_pattern.sub('', idx)

    # 6. Replace Footer with standardized identical footer
    footer_pattern = re.compile(r'<!-- =+\s*Footer.*?</footer>', re.DOTALL)
    idx = footer_pattern.sub(get_footer().strip(), idx)

    with open(os.path.join(SITE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(idx)
    print("Updated: index.html (logo, hero, removed calculator, removed upfront card, removed prices, unified footer)")

def update_utility_pages():
    for fname in ["about.html", "contact-urban-shine-perth.html", "book.html"]:
        fpath = os.path.join(SITE_DIR, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Favicon
        if '<link rel="icon"' not in content:
            content = content.replace('</title>', '</title>\n  <link rel="icon" type="image/png" href="assets/images/logo-emblem.png">')
        else:
            content = re.sub(r'<link rel="icon"[^>]*>', '<link rel="icon" type="image/png" href="assets/images/logo-emblem.png">', content)

        # Header logo
        content = re.sub(r'<a href="index\.html" class="brand-logo"[^>]*>.*?</a>',
                         '''<a href="index.html" class="brand-logo" aria-label="Urban Shine Homepage">
        <img src="assets/images/logo-emblem.png" alt="Urban Shine Emblem" class="brand-emblem-img" style="height: 46px; width: auto; object-fit: contain;">
        <div class="brand-text-block">
          <div class="brand-title">URBAN<span>SHINE</span></div>
          <div class="brand-subtitle">HOME SERVICE</div>
        </div>
      </a>''', content, flags=re.DOTALL)

        # Replace footer
        content = re.sub(r'<!-- Universal UrbanX Footer -->.*?</footer>|<!-- =+\s*Footer.*?</footer>|<footer class="main-footer".*?</footer>|<footer class="site-footer".*?</footer>',
                         get_footer().strip(), content, flags=re.DOTALL)

        # In book.html: remove dollar calculation display
        if fname == "book.html":
            content = re.sub(r'<div class="calculated-price-range">.*?</div>',
                             '<div class="calculated-price-range"><span id="bookCalcMin">Transparent</span> – <span id="bookCalcMax">On-Site Quote</span></div>', content, flags=re.DOTALL)
            content = re.sub(r'<span id="bookPriceDisplay">.*?</span>',
                             '<span id="bookPriceDisplay">Custom On-Site Quote</span>', content)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {fname} (logo, unified footer)")

if __name__ == "__main__":
    print("1. Regenerating all 12 dedicated service pages (No Prices, New Logo, Unified Footer)...")
    for s in SERVICES_META:
        generate_service_page(s)

    print("2. Regenerating Services Directory page...")
    generate_services_directory_page()

    print("3. Updating index.html (Hero, Logo, No Calc, No Upfront Card, No Prices, Unified Footer)...")
    update_index_page()

    print("4. Updating About, Contact, and Book pages with New Logo and Unified Footer...")
    update_utility_pages()

    print("\nAll 17 pages successfully updated and unified!")
