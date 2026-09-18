# Notice and methodological attribution

Authorial Editor is an independent open-source project inspired by the methodology described in:

Jenna Russell, Rishanth Rajendhran, Chau Minh Pham, Mohit Iyyer, and John Wieting.
**StoryScope: Investigating idiosyncrasies in AI fiction.**
COLM 2026. arXiv:2604.03136.

Official StoryScope repository:
https://github.com/jenna-russell/storyscope

StoryScope is released under the MIT License.


## Project licensing / Licenza del progetto

**EN**  
Authorial Editor is licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only). The full license text is provided in `LICENSE`.

Authorial Editor is an independent project and is not affiliated with, endorsed by, or sponsored by n8n GmbH. The workflow definitions in this repository are part of Authorial Editor; the n8n software itself remains subject to n8n's own licensing terms.

**IT**  
Authorial Editor è distribuito secondo i termini della GNU Affero General Public License v3.0 only (AGPL-3.0-only). Il testo completo della licenza è disponibile nel file `LICENSE`.

Authorial Editor è un progetto indipendente e non è affiliato, approvato o sponsorizzato da n8n GmbH. Le definizioni dei workflow presenti in questa repository fanno parte di Authorial Editor; il software n8n resta soggetto ai propri termini di licenza.

## What is adapted

Authorial Editor adapts high-level methodological ideas including:

- separating discourse-level structure from surface style;
- using structured intermediate representations;
- applying interpretable feature dimensions;
- analysing dimensions in separate stages rather than relying on one monolithic call;
- treating feature definitions as inspectable data.

## What is not claimed

The StoryScope paper studies long-form fiction. Authorial Editor applies related ideas to editorial and non-fiction text.

Therefore:

- the editorial taxonomy in this repository is not claimed to be validated by StoryScope;
- StoryScope's human-vs-AI classification results must not be treated as performance estimates for Authorial Editor;
- Authorial Editor does not claim that its feature scores identify human or AI authorship;
- Authorial Editor does not currently incorporate or redistribute the StoryScope training data, human stories, trained classifiers, or source code.

Any future direct code reuse from StoryScope must retain the attribution and license notices required by its MIT License.
