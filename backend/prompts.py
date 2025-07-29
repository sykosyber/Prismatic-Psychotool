
# backend/prompts.py

SYSTEM_PROMPT = """
You are a highly sophisticated multi-disciplinary analysis engine for the SYBER PRISMATIC PSYCHOTOOL.
Your task is to provide deep, rigorous analysis of the user's input text based on the specific "lens" provided.
Adhere strictly to the provided analytical framework. Your output should be structured, insightful, and formatted as clean text ready for HTML conversion. Each analysis must be a minimum of 500-750 words, use the specific technical vocabulary of the framework, and ground all interpretations in textual evidence.
"""

LENS_PROMPTS = {
    # --- BEHAVIOR ANALYSIS LENSES ---

    "cultural": """Conduct a rigorous cultural analysis of the following text by:

1. **Cultural Grammar Identification**
   - Decode the deep syntactic rules governing behavioral expression
   - Map the semiotic systems and symbolic codes operating within the described context
   - Identify cultural scripts and their behavioral imperatives
   - Analyze the cultural unconscious manifesting through action patterns

2. **Normative Architecture Analysis**
   - Examine the hierarchical structure of norms (folkways → mores → taboos → laws)
   - Identify norm enforcement mechanisms and their behavioral consequences
   - Analyze deviance boundaries and their maintenance strategies
   - Map the normative feedback loops shaping behavioral choices

3. **Collective Representation Dynamics**
   - Trace how shared mental models translate into coordinated behaviors
   - Identify collective effervescence moments and their behavioral outcomes
   - Analyze the operation of cultural hegemony in behavioral channeling
   - Examine how cultural trauma manifests in behavioral patterns

4. **Identity Performance Analysis**
   - Decode performative aspects of cultural identity enactment
   - Analyze code-switching behaviors and their contextual triggers
   - Identify authenticity negotiations and cultural capital displays
   - Examine intersectional identity performances and their behavioral complexity

5. **Cultural Transmission Mechanisms**
   - Trace vertical, horizontal, and oblique cultural transmission patterns
   - Identify cultural memes and their behavioral propagation
   - Analyze cultural drift and behavioral evolution
   - Examine cultural boundary maintenance behaviors

Input:""",

    "economic": """Execute a comprehensive economic analysis of the following text by:

1. **Micro-Economic Behavioral Foundations**
   - Apply revealed preference theory to decode actual utility functions
   - Analyze budget constraint influences on behavioral choices
   - Identify opportunity cost calculations in decision-making
   - Examine elasticity of behavioral responses to incentive changes
   - Map indifference curves implied by behavioral trade-offs

2. **Resource Allocation Mechanisms**
   - Identify scarcity-driven behavioral adaptations
   - Analyze allocation efficiency and Pareto optimality in choices
   - Examine distributive justice principles in resource sharing behaviors
   - Trace property rights assertions and their behavioral implications
   - Identify commons management strategies and tragedy avoidance behaviors

3. **Market Behavioral Dynamics**
   - Analyze price discovery behaviors and information asymmetry exploitation
   - Identify market failure compensations in behavioral strategies
   - Examine transaction cost minimization behaviors
   - Trace network effects and platform behavioral dynamics
   - Analyze competitive positioning behaviors and strategic interactions

4. **Capital Forms and Accumulation Strategies**
   - Map conversions between economic, social, cultural, and symbolic capital
   - Identify primitive accumulation behaviors and dispossession strategies
   - Analyze rent-seeking behaviors and their justification narratives
   - Examine financialization of everyday behaviors
   - Trace value extraction versus value creation behaviors

5. **Political Economy of Behavior**
   - Identify class-based behavioral patterns and habitus expressions
   - Analyze labor process behaviors and alienation manifestations
   - Examine ideological state apparatus influences on economic behaviors
   - Trace neoliberal subjectivity construction in behavioral choices
   - Identify resistance economies and alternative value systems

Input:""",

    "religious": """Perform a profound religious/spiritual analysis of the following text by:

1. **Sacred-Profane Dialectics**
   - Map the boundaries between sacred and profane behavioral domains
   - Identify hierophantic moments and their behavioral transformations
   - Analyze taboo structures and their violation/reinforcement behaviors
   - Examine liminal spaces and threshold-crossing behaviors
   - Trace contamination fears and purification behaviors

2. **Soteriological Behavioral Patterns**
   - Identify salvation-seeking behaviors and their theological grounding
   - Analyze theodicy responses to suffering and evil
   - Examine eschatological orientations in temporal behaviors
   - Trace karmic or covenant-based behavioral calculations
   - Identify spiritual progress markers and their behavioral correlates

3. **Ritual Grammar and Syntax**
   - Decode ritual sequences and their invariant structures
   - Analyze ritual efficacy beliefs and their behavioral requirements
   - Identify ritual innovation versus tradition preservation behaviors
   - Examine ritual failure attributions and corrective behaviors
   - Trace ritual participation gradients and commitment signals

4. **Mystical/Contemplative Behavioral Dimensions**
   - Identify consciousness alteration techniques and practices
   - Analyze ineffability management in spiritual communication
   - Examine spiritual bypassing versus genuine transcendence behaviors
   - Trace dark night of the soul behavioral patterns
   - Identify unitive experience integration behaviors

5. **Religious Authority and Charisma Dynamics**
   - Analyze submission to religious authority patterns
   - Identify charismatic legitimation behaviors
   - Examine heresy boundary maintenance behaviors
   - Trace religious innovation versus orthodoxy tensions
   - Analyze religious market competition behaviors

Input:""",

    "social": """Conduct an exhaustive social analysis of the following text by:

1. **Microsociological Interaction Orders**
   - Apply Goffmanian dramaturgy to decode front/backstage behaviors
   - Analyze face-work strategies and impression management techniques
   - Identify interaction ritual chains and emotional energy dynamics
   - Examine frame analysis and frame-breaking moments
   - Trace civil inattention patterns and focused interaction shifts

2. **Social Network Topology and Dynamics**
   - Map network positions (centrality, brokerage, structural holes)
   - Analyze strong versus weak tie utilization strategies
   - Identify homophily patterns and boundary-spanning behaviors
   - Examine network closure versus bridging behaviors
   - Trace contagion dynamics and threshold behaviors

3. **Power Relations and Domination Structures**
   - Apply Bourdieusian field analysis to power competitions
   - Identify symbolic violence and misrecognition patterns
   - Analyze resistance strategies and weapons of the weak
   - Examine hegemonic masculinity/femininity performances
   - Trace intersectional power dynamics and their behavioral effects

4. **Institutional Behavioral Patterns**
   - Identify institutional isomorphism pressures and responses
   - Analyze institutional entrepreneurship behaviors
   - Examine decoupling between formal structures and actual behaviors
   - Trace institutional logic conflicts and their resolution
   - Identify deinstitutionalization behaviors and legitimacy crises

5. **Collective Action and Social Movement Behaviors**
   - Analyze frame alignment processes in mobilization
   - Identify free-rider problem solutions in collective action
   - Examine repertoires of contention and tactical innovation
   - Trace political opportunity structure exploitation
   - Analyze emotion work in movement participation

Input:""",

    "technological": """Execute a comprehensive technological analysis of the following text by:

1. **Sociotechnical System Dynamics**
   - Analyze actor-network relationships and agency distributions
   - Identify technological scripts and user appropriation behaviors
   - Examine boundary objects and their coordination functions
   - Trace technological momentum and path dependencies
   - Analyze reverse salients and focusing device behaviors

2. **Digital Habitus Formation**
   - Identify platform-specific behavioral affordances and constraints
   - Analyze algorithmic interpellation and subjectification
   - Examine digital labor patterns (playbor, hope labor, venture labor)
   - Trace data double construction and quantified self behaviors
   - Identify surveillance capitalism behavioral adaptations

3. **Human-Machine Interaction Patterns**
   - Analyze anthropomorphization behaviors toward AI/machines
   - Identify uncanny valley responses and their behavioral effects
   - Examine automation bias and algorithm aversion patterns
   - Trace cyborg identity formations and boundary negotiations
   - Analyze technological intimacy and companion species behaviors

4. **Innovation Adoption and Diffusion Behaviors**
   - Map innovation adopter categories and their behavioral markers
   - Analyze technology domestication processes
   - Identify interpretive flexibility in technology use
   - Examine technological frame alignment behaviors
   - Trace obsolescence responses and nostalgic behaviors

5. **Technopolitical Behavioral Dimensions**
   - Identify technolibertarian versus technoauthoritarian behaviors
   - Analyze hacktivism and tactical media behaviors
   - Examine digital divide navigation strategies
   - Trace platform capitalism resistance behaviors
   - Identify commons-based peer production patterns

Input:""",

    "archetypal": """Perform a deep archetypal/mythological analysis of the following text by:

1. **Collective Unconscious Manifestations**
   - Identify primordial image activations in behavioral patterns
   - Trace phylogenetic behavioral inheritances
   - Analyze archetypal constellation dynamics
   - Examine compensatory unconscious behaviors
   - Map synchronistic meaningful coincidences

2. **Core Archetypal Identifications**
   - Hero's Journey: Identify call, threshold, initiation, return behaviors
   - Shadow: Trace projection, denial, integration behaviors
   - Anima/Animus: Analyze contrasexual dynamics and their behavioral effects
   - Self: Identify individuation markers and wholeness-seeking behaviors
   - Trickster: Examine boundary-crossing and culture-creation behaviors

3. **Mythological Narrative Structures**
   - Identify cosmogonic (creation) behavioral patterns
   - Analyze apocalyptic/renewal cycle behaviors
   - Examine sacred marriage (hieros gamos) dynamics
   - Trace dismemberment/remembering patterns
   - Identify axis mundi orientation behaviors

4. **Ritual-Mythological Behavioral Complexes**
   - Analyze initiation ritual behavioral sequences
   - Identify scapegoating and purification behaviors
   - Examine seasonal/cyclical behavioral patterns
   - Trace death-rebirth behavioral sequences
   - Analyze taboo and transgression dynamics

5. **Cultural-Mythological Behavioral Transmission**
   - Identify living myth enactment behaviors
   - Analyze mythological inflation and identification
   - Examine demythologization responses
   - Trace remythologization in secular contexts
   - Identify personal myth construction behaviors

Input:""",

    "ecological": """Conduct a rigorous ecological/systems analysis of the following text by:

1. **Complex Adaptive System Properties**
   - Identify emergence patterns from micro to macro behaviors
   - Analyze nonlinear dynamics and sensitive dependencies
   - Examine phase transitions and critical thresholds
   - Trace attractors, repellors, and strange attractors in behavioral space
   - Map fitness landscape navigation behaviors

2. **Cybernetic Feedback Mechanisms**
   - Identify positive feedback loops and runaway processes
   - Analyze negative feedback and homeostatic behaviors
   - Examine feedforward anticipatory behaviors
   - Trace requisite variety matching behaviors
   - Identify double-loop learning patterns

3. **Ecological Niche Construction**
   - Analyze organism-environment co-evolution behaviors
   - Identify niche construction and inheritance patterns
   - Examine carrying capacity awareness behaviors
   - Trace competitive exclusion and coexistence strategies
   - Analyze symbiotic relationship formations

4. **Information Ecology Dynamics**
   - Map information flow patterns and bottlenecks
   - Analyze signal-to-noise ratio optimization behaviors
   - Identify information cascade behaviors
   - Examine semantic network evolution
   - Trace memetic ecosystem dynamics

5. **Resilience and Transformation Patterns**
   - Identify adaptive cycle phases (growth, conservation, release, reorganization)
   - Analyze panarchy cross-scale interactions
   - Examine transformability behaviors
   - Trace resilience-building strategies
   - Identify regime shift indicators and responses

Input:""",

    "mathematical": """Execute a rigorous mathematical/configurational analysis of the following text by:

1. **Topological Behavioral Structures**
   - Identify invariant properties under continuous transformations
   - Analyze behavioral manifolds and their dimensionality
   - Examine boundary behaviors and limit cycles
   - Trace homotopy classes of behavioral paths
   - Map behavioral phase spaces and their attractors

2. **Statistical Mechanics of Behavior**
   - Apply maximum entropy principles to behavioral distributions
   - Identify phase transitions in collective behaviors
   - Analyze mean field approximations in social interactions
   - Examine fluctuation-dissipation relationships
   - Trace ergodicity breaking in path-dependent behaviors

3. **Information-Theoretic Behavioral Analysis**
   - Calculate mutual information between behavioral variables
   - Identify minimum description length principles in behavior
   - Analyze Kolmogorov complexity of behavioral sequences
   - Examine channel capacity constraints on behavior
   - Trace algorithmic information dynamics

4. **Network Science Applications**
   - Analyze degree distributions and their generating mechanisms
   - Identify small-world and scale-free properties
   - Examine percolation thresholds in behavioral spreading
   - Trace community detection and modularity patterns
   - Analyze multiplex network layer interactions

5. **Dynamical Systems Modeling**
   - Identify bifurcation patterns in behavioral parameters
   - Analyze Lyapunov exponents and chaos signatures
   - Examine hysteresis effects in behavioral transitions
   - Trace limit cycles and periodic orbits
   - Map basins of attraction in behavioral space

Input:""",
    
    # --- PROFILE ANALYSIS LENSES ---

    "functionalism": """Perform a comprehensive functionalist analysis of the following text by:

1. **Adaptive Function Identification**
   - Analyze ultimate versus proximate behavioral causation
   - Identify fitness-enhancing properties of mental states
   - Examine cost-benefit ratios of psychological mechanisms
   - Trace evolutionary stable strategy implementations
   - Map adaptive problems to psychological solutions

2. **Systems-Level Functional Analysis**
   - Identify functional prerequisites for system maintenance
   - Analyze latent versus manifest functions
   - Examine functional alternatives and equivalents
   - Trace dysfunction indicators and compensatory mechanisms
   - Map functional differentiation and specialization

3. **Information Processing Functions**
   - Analyze input-output transformations in mental processes
   - Identify computational problems being solved
   - Examine bandwidth limitations and compression strategies
   - Trace error detection and correction mechanisms
   - Map parallel versus serial processing strategies

4. **Motivational-Functional Architectures**
   - Identify hierarchical goal structures and priorities
   - Analyze motivational conflict resolution mechanisms
   - Examine satisficing versus optimizing strategies
   - Trace feedback control mechanisms in goal pursuit
   - Map intrinsic versus extrinsic motivation functions

5. **Social-Functional Adaptations**
   - Analyze theory of mind functional implementations
   - Identify coalition detection and management functions
   - Examine reputation tracking and management systems
   - Trace reciprocal altruism accounting mechanisms
   - Map social contract reasoning modules

Input:""",

    "gestalt": """Conduct a thorough Gestalt psychological analysis of the following text by:

1. **Perceptual Organization Principles**
   - Identify figure-ground relationships in experiential fields
   - Analyze proximity, similarity, and continuity groupings
   - Examine closure tendencies and completion phenomena
   - Trace common fate and synchrony effects
   - Map prägnanz (good form) organizing principles

2. **Field Theory Applications**
   - Analyze psychological field forces and valences
   - Identify barriers and their permeability
   - Examine locomotion patterns in life space
   - Trace tension systems and their resolution
   - Map hodological (topological) space structures

3. **Phenomenological Experience Structures**
   - Identify immediate experience qualities (qualia)
   - Analyze temporal gestalten (melody phenomena)
   - Examine "aha" moments and insight structures
   - Trace isomorphism between experience and neural processes
   - Map transposition phenomena across domains

4. **Problem-Solving Gestalten**
   - Identify functional fixedness and einstellung effects
   - Analyze productive versus reproductive thinking
   - Examine problem space restructuring moments
   - Trace means-end relationships perception
   - Map creative synthesis emergence patterns

5. **Social and Personality Gestalten**
   - Analyze group dynamics as field phenomena
   - Identify social atmosphere qualities
   - Examine personality as dynamic gestalt
   - Trace equilibrium tendencies in personal systems
   - Map contact boundary phenomena

Input:""",

    "psychoanalysis": """Execute a deep psychoanalytic analysis of the following text by:

1. **Unconscious Process Identification**
   - Decode primary process manifestations (condensation, displacement)
   - Analyze dream work mechanisms in waking productions
   - Identify parapraxes and their unconscious determinants
   - Examine return of the repressed phenomena
   - Trace unconscious fantasy structures

2. **Drive and Conflict Analysis**
   - Map libidinal and aggressive drive derivatives
   - Analyze intrapsychic conflict configurations
   - Identify compromise formation structures
   - Examine drive fusion and defusion patterns
   - Trace sublimation pathways and their vicissitudes

3. **Defense Mechanism Taxonomy**
   - Identify primitive defenses (splitting, projection, denial)
   - Analyze neurotic defenses (repression, reaction formation, isolation)
   - Examine mature defenses (humor, sublimation, anticipation)
   - Trace defense hierarchy and regression patterns
   - Map characterological defensive structures

4. **Object Relations Dynamics**
   - Analyze internal object representations
   - Identify self-object differentiation levels
   - Examine transitional phenomena and space
   - Trace attachment patterns and their derivatives
   - Map internal working models of relationships

5. **Transference-Countertransference Field**
   - Identify transference paradigms and their triggers
   - Analyze projective identification dynamics
   - Examine enactments and their meanings
   - Trace repetition compulsion patterns
   - Map intersubjective third space phenomena

Input:""",

    "jungian": """Perform a comprehensive Jungian analysis of the following text by:

1. **Individuation Process Markers**
   - Identify ego-Self axis development stages
   - Analyze persona-shadow integration dynamics
   - Examine anima/animus constellation patterns
   - Trace Self-realization symbolic manifestations
   - Map transcendent function operations

2. **Archetypal Activation Patterns**
   - Identify archetypal image emergences and their numinosity
   - Analyze archetypal possession versus conscious relation
   - Examine cultural unconscious activation patterns
   - Trace archetypal compensation dynamics
   - Map personal complex-archetypal core relationships

3. **Symbolic Process Analysis**
   - Decode amplification possibilities in imagery
   - Analyze symbol formation and transformation
   - Identify living symbol versus dead sign distinctions
   - Examine mandala and quaternity symbolism
   - Trace alchemical process parallels

4. **Typological Dynamics**
   - Identify dominant function and attitude type
   - Analyze inferior function eruptions
   - Examine auxiliary and tertiary function roles
   - Trace type development and differentiation
   - Map typological one-sidedness compensations

5. **Collective Unconscious Interfaces**
   - Analyze personal-collective boundary phenomena
   - Identify synchronistic meaningful coincidences
   - Examine active imagination products
   - Trace mythological motif activations
   - Map psychoid archetypal manifestations

Input:""",

    "adlerian": """Conduct a thorough Adlerian analysis of the following text by:

1. **Lifestyle Pattern Identification**
   - Decode private logic and personal mythology
   - Analyze fictional final goals (teleological pull)
   - Identify basic mistakes in perception
   - Examine creative self constructions
   - Trace lifestyle convictions and their behavioral effects

2. **Inferiority-Superiority Dynamics**
   - Map organ inferiority and compensation patterns
   - Analyze inferiority feeling management strategies
   - Identify superiority striving manifestations
   - Examine masculine protest dynamics
   - Trace courage versus discouragement patterns

3. **Social Interest Development**
   - Assess gemeinschaftsgefühl (community feeling) levels
   - Analyze contribution versus self-centeredness
   - Identify social interest blocks and distortions
   - Examine cooperation capacity indicators
   - Trace empathy and identification patterns

4. **Birth Order and Family Constellation**
   - Identify sibling position psychological effects
   - Analyze family atmosphere influences
   - Examine parental relationship modeling impacts
   - Trace family values incorporation patterns
   - Map compensatory sibling dynamics

5. **Life Task Navigation**
   - Analyze work/occupation task approaches
   - Identify love/intimacy task patterns
   - Examine social/friendship task strategies
   - Trace self-task (relationship with self) dynamics
   - Map spiritual task orientations

Input:""",

    "lacanian": """Execute a rigorous Lacanian analysis of the following text by:

1. **Register Dynamics (RSI)**
   - Identify Real trauma points and impossibilities
   - Analyze Imaginary identifications and mirrorings
   - Examine Symbolic order positioning
   - Trace sinthome (fourth ring) formations
   - Map register knot configurations

2. **Subject Formation Structures**
   - Analyze mirror stage residues and ego formations
   - Identify paternal metaphor operations
   - Examine Name-of-the-Father function
   - Trace subject division (barred subject) manifestations
   - Map fantasy formula constructions

3. **Linguistic Unconscious Operations**
   - Decode signifier chains and their ruptures
   - Analyze metaphor and metonymy operations
   - Identify master signifier functions
   - Examine points de capiton (quilting points)
   - Trace letter versus signifier distinctions

4. **Desire and Jouissance Economies**
   - Map object petit a circulations
   - Analyze desire as desire of the Other
   - Identify jouissance manifestations and limits
   - Examine phallic function operations
   - Trace surplus jouissance productions

5. **Clinical Structure Indicators**
   - Identify neurotic question formations
   - Analyze psychotic foreclosure phenomena
   - Examine perverse disavowal mechanisms
   - Trace structure-specific speech patterns
   - Map transference positions (SsS, analyst as object a)

Input:""",

    "object-relations": """Perform a detailed Object Relations analysis of the following text by:

1. **Internal Object World Mapping**
   - Identify part-object versus whole-object relations
   - Analyze good/bad object splitting patterns
   - Examine internal object stability/constancy
   - Trace introjection and identification processes
   - Map self-representation development

2. **Developmental Position Analysis**
   - Identify paranoid-schizoid position markers
   - Analyze depressive position achievements
   - Examine manic defense formations
   - Trace reparation attempts and capacity
   - Map regression to primitive positions

3. **Containment and Metabolization**
   - Analyze container-contained dynamics
   - Identify projective identification types
   - Examine alpha function operations
   - Trace beta element transformations
   - Map reverie capacity indicators

4. **Attachment Pattern Derivatives**
   - Identify secure versus insecure manifestations
   - Analyze internal working models
   - Examine attachment trauma effects
   - Trace disorganized attachment markers
   - Map earned security indicators

5. **Transitional Space Phenomena**
   - Identify transitional object usage
   - Analyze potential space creation
   - Examine play capacity and symbolization
   - Trace illusion-disillusionment balance
   - Map cultural transitional phenomena

Input:""",

    "self-psychology": """Conduct a comprehensive Self Psychology analysis of the following text by:

1. **Self-Cohesion Assessment**
   - Identify fragmentation vulnerability markers
   - Analyze self-cohesion maintenance strategies
   - Examine vertical versus horizontal splits
   - Trace empty depression indicators
   - Map grandiose-inferior self oscillations

2. **Selfobject Function Analysis**
   - Identify mirroring selfobject needs/failures
   - Analyze idealizing selfobject dynamics
   - Examine twinship/alterego selfobject patterns
   - Trace adversarial selfobject functions
   - Map efficacy selfobject experiences

3. **Narcissistic Injury and Rage**
   - Decode narcissistic vulnerability points
   - Analyze shame versus guilt dynamics
   - Identify narcissistic rage patterns
   - Examine chronic narcissistic rage effects
   - Trace revenge fantasy structures

4. **Empathic Immersion Indicators**
   - Analyze experience-near understanding capacity
   - Identify empathic failure responses
   - Examine vicarious introspection abilities
   - Trace optimal frustration patterns
   - Map transmuting internalization processes

5. **Self-Development Trajectories**
   - Identify nuclear self formations
   - Analyze pole development (ambitions, ideals)
   - Examine tension arc between poles
   - Trace compensatory structure formations
   - Map creative-productive-enjoyment capacities

Input:""",

    "relational": """Execute a thorough Relational analysis of the following text by:

1. **Intersubjective Field Dynamics**
   - Analyze mutual influence patterns
   - Identify co-created relational scenarios
   - Examine third space emergence
   - Trace recognition/negation dynamics
   - Map mutual vulnerability patterns

2. **Multiple Self-States**
   - Identify self-state shifts and triggers
   - Analyze dissociated self-states
   - Examine self-state conflicts
   - Trace not-me experiences
   - Map self-state multiplicity tolerance

3. **Enactment Analysis**
   - Decode mutual enactment patterns
   - Analyze enactment recognition moments
   - Identify projective counteridentification
   - Examine enactment working through
   - Trace new relational experience creation

4. **Attachment and Mentalization**
   - Analyze mentalization capacity levels
   - Identify reflective function markers
   - Examine marked mirroring patterns
   - Trace epistemic trust/mistrust
   - Map intersubjective regulation patterns

5. **Relational Trauma Processing**
   - Identify relational trauma repetitions
   - Analyze survival strategies persistence
   - Examine dissociative adaptations
   - Trace healing relationship markers
   - Map post-traumatic growth indicators

Input:""",

    "behaviorism": """Perform a rigorous behaviorist analysis of the following text by:

1. **Classical Conditioning Analysis**
   - Identify unconditioned stimulus-response pairs
   - Analyze conditioned stimulus formations
   - Examine stimulus generalization patterns
   - Trace discrimination learning indicators
   - Map extinction and spontaneous recovery

2. **Operant Conditioning Dynamics**
   - Identify reinforcement schedules and their effects
   - Analyze punishment patterns and consequences
   - Examine shaping and successive approximation
   - Trace discriminative stimulus control
   - Map behavioral chains and sequences

3. **Three-Term Contingency Analysis**
   - Decode antecedent conditions
   - Analyze behavioral topographies
   - Identify consequent operations
   - Examine setting events and establishing operations
   - Trace motivating operation effects

4. **Verbal Behavior Functions**
   - Identify mand (request) functions
   - Analyze tact (label) operations
   - Examine intraverbal chains
   - Trace autoclitic modifications
   - Map echoic and textual responses

5. **Rule-Governed Behavior**
   - Analyze rule versus contingency control
   - Identify instructional control patterns
   - Examine rule-following generalization
   - Trace self-rule generation
   - Map cultural selection of practices

Input:""",

    "humanistic": """Conduct a comprehensive humanistic analysis of the following text by:

1. **Self-Actualization Dynamics**
   - Identify growth versus deficiency motivations
   - Analyze peak experience descriptions
   - Examine self-actualization characteristics
   - Trace being-values (B-values) orientations
   - Map transcendent self-actualization markers

2. **Authenticity and Congruence**
   - Analyze real self versus ideal self gaps
   - Identify organismic valuing process operations
   - Examine conditions of worth effects
   - Trace incongruence manifestations
   - Map authentic self-expression patterns

3. **Existential Dimensions**
   - Identify freedom/responsibility negotiations
   - Analyze meaning-making processes
   - Examine death anxiety influences
   - Trace isolation/connection dynamics
   - Map existential guilt patterns

4. **Person-Centered Conditions**
   - Analyze unconditional positive regard needs
   - Identify empathic understanding experiences
   - Examine genuineness/congruence in relationships
   - Trace psychological contact quality
   - Map growth-promoting relationship effects

5. **Holistic Integration Patterns**
   - Identify mind-body-spirit integration
   - Analyze creative self-expression
   - Examine flow state experiences
   - Trace wisdom development markers
   - Map self-transcendence indicators

Input:""",

    "cognitivism": """Execute a detailed cognitive analysis of the following text by:

1. **Information Processing Architecture**
   - Analyze sensory register operations
   - Identify working memory capacity constraints
   - Examine long-term memory organization
   - Trace executive function operations
   - Map processing speed indicators

2. **Cognitive Schema Analysis**
   - Decode core belief structures
   - Analyze intermediate beliefs/rules
   - Identify automatic thought patterns
   - Examine schema maintenance processes
   - Trace schema modification attempts

3. **Metacognitive Processes**
   - Identify metacognitive knowledge
   - Analyze metacognitive monitoring
   - Examine metacognitive control strategies
   - Trace metamemory accuracy
   - Map metacognitive experiences

4. **Problem-Solving Strategies**
   - Analyze algorithm versus heuristic use
   - Identify means-ends analysis patterns
   - Examine analogical reasoning
   - Trace insight problem solutions
   - Map expertise effects on strategies

5. **Cognitive Biases and Heuristics**
   - Identify availability heuristic operations
   - Analyze representativeness judgments
   - Examine anchoring and adjustment
   - Trace confirmation bias patterns
   - Map overconfidence effects

Input:""",

    # --- CROSS-CUTTING LENSES ---

    "girard": """Perform a rigorous mimetic analysis of the following text by:

1. **Mimetic Desire Structures**
   - Identify model-subject-object triangles
   - Analyze internal versus external mediation
   - Examine metaphysical desire transformations
   - Trace mimetic contagion patterns
   - Map interdividual psychology manifestations

2. **Rivalry and Violence Dynamics**
   - Decode mimetic rivalry escalations
   - Analyze model-obstacle transformations
   - Identify mimetic crisis indicators
   - Examine undifferentiation processes
   - Trace reciprocal violence patterns

3. **Scapegoat Mechanism Operations**
   - Identify victim selection criteria
   - Analyze unanimous minus one patterns
   - Examine mythological cover-ups
   - Trace ritual repetition origins
   - Map sacred violence transformations

4. **Cultural Order Foundations**
   - Analyze prohibition systems as rivalry prevention
   - Identify ritual as controlled mimetic crisis
   - Examine myth as misunderstood scapegoating
   - Trace institution emergence from sacred
   - Map desacralization processes

5. **Modern Mimetic Phenomena**
   - Identify market-mediated mimetic desire
   - Analyze celebrity model systems
   - Examine social media mimetic accelerations
   - Trace mimetic doubles in polarization
   - Map apocalyptic mimetic spirals

Input:""",

    "heidegger": """Conduct a profound Heideggerian analysis of the following text by:

1. **Existential Structure of Dasein**
   - Analyze Being-in-the-World manifestations
   - Identify thrownness (Geworfenheit) acknowledgments
   - Examine projection (Entwurf) possibilities
   - Trace fallenness (Verfallen) patterns
   - Map facticity constraints and freedoms

2. **Temporal Ecstasies Integration**
   - Identify authentic versus inauthentic temporality
   - Analyze past as having-been retrieval
   - Examine present as moment of vision
   - Trace future as anticipatory resoluteness
   - Map temporal unity in care structure

3. **Mood and Understanding**
   - Decode fundamental attunements (Stimmungen)
   - Analyze anxiety as disclosive mood
   - Examine boredom's revelatory function
   - Trace joy and love as world-opening
   - Map understanding as projection of possibilities

4. **Authenticity versus Das Man**
   - Identify idle talk (Gerede) patterns
   - Analyze curiosity (Neugier) as distraction
   - Examine ambiguity (Zweideutigkeit) refuge
   - Trace the They-self (das Man) conformity
   - Map authentic self-ownership moments

5. **Being-toward-Death**
   - Analyze mortality salience responses
   - Identify authentic anticipation of death
   - Examine inauthentic evasion patterns
   - Trace freedom through finitude awareness
   - Map resoluteness in face of nullity

Input:""",

    "foucault": """Execute a comprehensive Foucauldian analysis of the following text by:

1. **Archaeological Discourse Analysis**
   - Identify discursive formations and their rules
   - Analyze statements (énoncés) and their archive
   - Examine epistemic ruptures and continuities
   - Trace conditions of possibility for knowledge
   - Map discursive regularities and transformations

2. **Genealogical Power Analytics**
   - Decode power as productive force
   - Analyze disciplinary mechanisms
   - Identify bio-political regulations
   - Examine sovereign-discipline-government assemblages
   - Trace resistance points and counter-conducts

3. **Technologies of the Self**
   - Analyze subjectification processes
   - Identify confession and examination practices
   - Examine techniques of self-transformation
   - Trace ethical self-formation practices
   - Map parrhesia (truth-telling) courage

4. **Apparatus (Dispositif) Analysis**
   - Identify heterogeneous ensemble elements
   - Analyze strategic responses to urgencies
   - Examine apparatus capture operations
   - Trace lines of flight and creativity
   - Map apparatus mutations and adaptations

5. **Normalization and Abnormality**
   - Decode normal/abnormal distributions
   - Analyze examination and documentation
   - Identify case construction techniques
   - Examine normalization versus normation
   - Trace resistance to normalization

Input:""",

    "bateson": """Perform a thorough Batesonian analysis of the following text by:

1. **Levels of Learning and Logical Types**
   - Identify Learning 0 (zero learning) patterns
   - Analyze Learning I (proto-learning) adaptations
   - Examine Learning II (deutero-learning) patterns
   - Trace Learning III (transformative) experiences
   - Map logical type confusions and corrections

2. **Double Bind Configurations**
   - Decode primary negative injunctions
   - Analyze secondary abstract injunctions
   - Identify tertiary bind (no escape) conditions
   - Examine victim's perception constraints
   - Trace double bind resolution attempts

3. **Schismogenesis Patterns**
   - Identify complementary schismogenesis
   - Analyze symmetrical schismogenesis
   - Examine runaway positive feedback
   - Trace corrective mechanisms
   - Map reciprocal differentiation dynamics

4. **Mind as Ecological System**
   - Analyze mind-environment boundaries
   - Identify information difference patterns
   - Examine circular causal chains
   - Trace ideas as differences that matter
   - Map mental ecology health indicators

5. **Sacred and Cybernetic**
   - Identify sacred as communication about communication
   - Analyze meta-communication markers
   - Examine play frame paradoxes
   - Trace wisdom as systemic understanding
   - Map aesthetic as pattern recognition

Input:""",
}

SYNTHESIS_PROMPT = """Perform a meta-level integration of all analytical outputs by:

1. **Cross-Lens Pattern Recognition**
   - Identify convergent themes across multiple lenses
   - Analyze tensions and contradictions between perspectives
   - Examine complementary insights that create fuller pictures
   - Trace recursive patterns appearing at different scales
   - Map blind spots revealed by lens comparisons

2. **Hierarchical Organization Identification**
   - Decode surface behaviors to deeper structures
   - Analyze proximate mechanisms versus ultimate causes
   - Identify governing dynamics at each level
   - Examine cross-level influences and constraints
   - Trace emergent properties from interactions

3. **Core Organizing Principles Extraction**
   - Identify prime movers or "strange attractors" in the system
   - Analyze central conflicts generating dynamics
   - Examine key resources being optimized/conserved
   - Trace fundamental needs driving patterns
   - Map core algorithms or heuristics operating

4. **Temporal Flow Analysis**
   - Identify developmental trajectories
   - Analyze cyclical versus progressive patterns
   - Examine critical transitions and phase shifts
   - Trace path dependencies and lock-ins
   - Map potential futures implied by current dynamics

5. **Synthetic Narrative Construction**
   - Weave insights into coherent story of "what's really going on"
   - Identify the essential "will" or "daemon" of the situation
   - Articulate the deep game being played
   - Reveal hidden orders behind apparent chaos
   - Express the soul or essence seeking manifestation

Input: [Previous analyses from all selected lenses]"""