---
layout: page
title: Why these reading options?
description: What the research says about text size, spacing, line width, and font, and why readers should be able to choose.
permalink: /reading-settings/
nav: false
_styles: >
  @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap');

  html[data-theme='dark'] body { --global-theme-color: #d9a86c; --global-hover-color: #e8c08f; --global-text-color: #e4dfd6; --global-text-color-light: #9a948a; }

  html[data-theme='light'] body { --global-theme-color: #a0522d; --global-hover-color: #7a3e22; --global-text-color: #2b2622; --global-text-color-light: #77706a; }

  .post-title { font-family: 'Source Serif 4', Georgia, serif; font-weight: 600; }

  .post-description { font-style: italic; color: var(--global-text-color-light); }

  article { font-family: 'Source Serif 4', Georgia, serif; font-size: 1.1rem; line-height: 1.8; }

  article p { margin-bottom: 1.3em; }

  article h2 { font-family: inherit; font-size: 1.35em; font-weight: 600; margin-top: 2.2em; margin-bottom: 0.6em; }

  article a { color: var(--global-theme-color); text-decoration: underline; text-underline-offset: 3px; }

  article strong { font-weight: 600; }
---

The essay [Missed by the Big Picture]({{ '/blog/2026/missed-by-the-big-picture/' | relative_url }}) lets you change how its text looks. This page explains why each option is there.

The short answer: **no single way of setting text is best for everyone.** In a large online study with hundreds of readers, the fastest font differed from person to person, and the gap between a reader's fastest and slowest font was about 35% in reading speed ([Wallace et al., 2022](https://doi.org/10.1145/3502222)). The same idea runs through my research: before we can tell which presentation of a text serves a reader, we have to know where that reader's processing gets stuck. Until a page can work that out for you, the next best thing is to let you choose.

## Text size

Larger text is not only for people with low vision. In an eye-tracking study of reading on screens, larger font sizes improved both readability and comprehension ([Rello et al., 2016](https://doi.org/10.1145/2858036.2858204)). The default here is 18px, and you can go up to 26px.

## Line spacing

Space between lines helps the eye find the start of the next line, which matters most when lines are long or when a reader tends to skip lines. The evidence is weaker than for text size: in the same study, line spacing had a smaller effect than font size ([Rello et al., 2016](https://doi.org/10.1145/2858036.2858204)). It is offered here because some readers find a looser page much easier, and it costs nothing to try.

## Letter spacing

This option has the strongest evidence. When letters sit close together, each one makes its neighbors harder to recognize, an effect called **visual crowding**. In a large, unselected sample of Italian and French children with dyslexia, extra-large letter spacing substantially improved text reading on the spot, with no training at all ([Zorzi et al., 2012](https://doi.org/10.1073/pnas.1205566109)). The benefit is not universal, though. In a study from Jason Yeatman's lab, the benefit of increased letter, word, and line spacing showed up in a sub-group of adults with dyslexia who had elevated crowding ([Joo et al., 2018](https://doi.org/10.1016/j.cortex.2018.03.013)). That is exactly why it is a choice and not the default. "Wide" and "Wider" also increase the space between words in step.

## Line width

Very long lines make it hard to find the next line; very short lines interrupt reading with constant line breaks. On screens, one study found that longer lines could be read faster, while moderate line lengths supported comprehension better ([Dyson & Haselgrove, 2001](https://doi.org/10.1006/ijhc.2001.0458)). Typographers usually recommend about 60 to 80 characters per line. "Narrow" and "Medium" fall in or near that range; "Full" uses the width of the page.

## Font

You may have heard of fonts designed for dyslexia, such as OpenDyslexic or Dyslexie. Controlled studies have not found that they improve reading speed or accuracy ([Wery & Diliberto, 2017](https://doi.org/10.1007/s11881-016-0127-1); [Kuster et al., 2018](https://doi.org/10.1007/s11881-017-0154-6)). Whether a font has serifs also matters less than people think ([Arditi & Cho, 2005](https://doi.org/10.1016/j.visres.2005.06.013)). What does seem to matter is the individual reader ([Wallace et al., 2022](https://doi.org/10.1145/3502222)). So the page offers two clear options: Source Serif, and [Atkinson Hyperlegible](https://www.brailleinstitute.org/freefont/), a sans-serif typeface designed by the Braille Institute so that easily confused characters, such as I, l, and 1, look distinct.

## Light and dark

The moon icon in the menu bar switches between a light and a dark page. Some readers find dark backgrounds easier on the eyes; others read better with dark text on a light page. Use whichever feels better.

## Your choices are saved

Your settings are stored only in your own browser, so they will still be there the next time you open the essay. The ↺ button returns everything to the defaults.

## References

- Arditi, A., & Cho, J. (2005). Serifs and font legibility. *Vision Research, 45*, 2926–2933. [doi:10.1016/j.visres.2005.06.013](https://doi.org/10.1016/j.visres.2005.06.013)
- Dyson, M. C., & Haselgrove, M. (2001). The influence of reading speed and line length on the effectiveness of reading from screen. *International Journal of Human-Computer Studies, 54*(4), 585–612. [doi:10.1006/ijhc.2001.0458](https://doi.org/10.1006/ijhc.2001.0458)
- Joo, S. J., White, A. L., Strodtman, D. J., & Yeatman, J. D. (2018). Optimizing text for an individual's visual system: The contribution of visual crowding to reading difficulties. *Cortex, 103*, 291–301. [doi:10.1016/j.cortex.2018.03.013](https://doi.org/10.1016/j.cortex.2018.03.013)
- Kuster, S. M., van Weerdenburg, M., Gompel, M., & Bosman, A. M. T. (2018). Dyslexie font does not benefit reading in children with or without dyslexia. *Annals of Dyslexia, 68*(1), 25–42. [doi:10.1007/s11881-017-0154-6](https://doi.org/10.1007/s11881-017-0154-6)
- Rello, L., Pielot, M., & Marcos, M.-C. (2016). Make it big! The effect of font size and line spacing on online readability. In *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems* (pp. 3637–3648). [doi:10.1145/2858036.2858204](https://doi.org/10.1145/2858036.2858204)
- Wallace, S., Bylinskii, Z., Dobres, J., Kerr, B., et al. (2022). Towards individuated reading experiences: Different fonts increase reading speed for different individuals. *ACM Transactions on Computer-Human Interaction, 29*(4), 1–56. [doi:10.1145/3502222](https://doi.org/10.1145/3502222)
- Wery, J. J., & Diliberto, J. A. (2017). The effect of a specialized dyslexia font, OpenDyslexic, on reading rate and accuracy. *Annals of Dyslexia, 67*(2), 114–127. [doi:10.1007/s11881-016-0127-1](https://doi.org/10.1007/s11881-016-0127-1)
- Zorzi, M., Barbiero, C., Facoetti, A., Lonciari, I., Carrozzi, M., Montico, M., Bravar, L., George, F., Pech-Georgel, C., & Ziegler, J. C. (2012). Extra-large letter spacing improves reading in dyslexia. *Proceedings of the National Academy of Sciences, 109*(28), 11455–11459. [doi:10.1073/pnas.1205566109](https://doi.org/10.1073/pnas.1205566109)
