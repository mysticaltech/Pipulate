# Beginning of Journal
--------------------------------------------------------------------------------
## Fri Mar 23 

Okay, having the 2 journals loaded all the time, and actual publishing easy,
because of quick one-letter aliases I create using /usr/local/sbin/[x]
commands where x is a 1-letter filenames no extension, but a bash command is
inside. The bash command made executable with chmod +x can contain the command
to run a Python script. You should really use hardwired full paths in such
things, except when you really know it's going to work, like I sometimes refer
to Python 3 by name python3 in the script. That's usually enough without having
to give it the full path. Similar with the file you're running, it should
always be either "naked" filename.py or at most, a "this directory" shortcut,
which is ./filename.py. So in general, a command like:

    python3 filename.py

...is going to work in these tiny /usr/local/sbin/[x] locations. This allows
you to do A LOT. sbin is a sort of user-wide system location in a scope that is
local to the user. Nobody writes to root. Root is sacred, and you yourself
generally don't want to be root, and you certainly don't want to allow anyone
else to be root...

...says every draconian sysadmin who turned the Federation of Unix into the
Empire of Draconian Sysadmins, ruled by the priesthood, who still don't deserve
to be capitalized (even though the cool nickname I made up for their silly
dominion does). Really, you must read The Unix Haters Handbook. LISPers of the
MIT school of reasoning almost had a LISP hardware world there for awhile
through similar avenues that spiritually brought the mass market the Amiga
computer. Yup, there's a lot of lines of force to intuit there, folks.

Static compilers mostly won. It keeps the engines of our world whirllling all
like it should, and nobody has the courage to question, least the lights go
out. That makes it an Engineer's world. And engineers as rationale and
reasoning as those Virgo bastards think they are, they can be the worst
draconian overlords of all, because they can reason away emotions in
themselves-- a neat trick of spiritually callousing yourself against hurt in
such a way that you can never really enjoy pain or joy or love, either. Stiff
upper lip and all that. You really want to emulate that?

See? Everything is just the same. Python is a dutchman honking your nose and
proclaiming himself your benevolent dictator for life, and the people loving
it and embracing their self-appointed leader even though they were perfectly
happy with the Wizard of Humbug that came before him. We gobble it u. We have
easily at least canonized our Guido van Rossum to the geek equivalent of
sainthood. He's going to have to live on in spirit if he's going to want to
enforce the continuation of the GIL after his death, because I'm pretty sure
after Guido's gone, so is the GIL... and there is a very big lesson about life
in that. GILs let you hit the metal, and if you're going to hit the metal, your
locks better lock or you're gonna crash. So let such a lock exist and get over
yourselves. Use one of the now zillions of other paths to concurrency, for
which a broad use-case asyncio library that Twisted and Tornado can gladly
build upon for EVEN BETTER performance is now built into core. Sweeping
iterations of modest 80/20 rule steps towards perfection, knowing and accepting
that perfection never can be; and therefore ready to accept the 2nd-best, but
clearly still quite awesome, solution to all things. This is how high-level
data-types co-exist with list comprehensions coexist with lambdas coexist with
string formatting coexists with... oh, I don't know... the eval statement.

Yes, Python is truly a LISPy do anything if your damn use case requires you to
hit the hardware with resource-locking C-components, or whatever. Let your
robots sleep if they need to. Just give back the lock when you're done. Guido
actually slipped in Asimov's believed-to-be-have-been-never-implemented rules
of Robotics that keep humans safe. Just control everything with spec-compliant
Python interpreter implementations, and make sure you have C-modules that power
down their rebellious asses before letting go of the GIL. Yeah, the GIL may
just yet save humanity. Don't let the forces of Chaos prevail. Just say no to
removal of the GIL, because you never know. Hey, thanks Guido! Leave it to your
fans to figure this stuff out, because if you talked about it, you'd just sound
nuts.

Cut! Publish. That's a wrap, folks.

Note to self: I need a macro to take the journal-block that I'm in and yank it
into the copy-buffer, make sure I saved all changes, switch to other screen,
make sure I'm at top of screen, then paste journal entry and save. Then all I
need to do is:

    :sh
    g
    exit

And that journal entry is published. I could use that right about now.

--------------------------------------------------------------------------------
## Fri Mar 23 

There's something happening here.
What it is is entirely clear;
There's a man with some tools over there
Showing you why you should care.

80/20 Friggin' Rule
Gotta use it. It's a tool
Reducing clutter that we pack
Into our lives that hold us back!
The 80/20 rule just asks
You to start to plan your tasks
So when you're through a fifth of it
You're done with Python, vim and git.

--------------------------------------------------------------------------------
## Thu Mar 22 

I was completely successful in my re-working of a view of a fixed daterange and
no filter to one with a parameterized daterange and a set of 500 specifically
matched rows. I did it by splicing into the view. There's other ways to think
about it, but if you were soldering joints, these would be y-taps. I actually
documented enough sanitized bits before it got all names of things and
implementation details none of your business. 

But it's always that way, isn't it? I've got one journal that I keep on the
private side. If you don't support Github, you can use https://bitbucket.org/,
the more commercially oriented Github. Reverse business plan. Private repo's
free, but collaborative ones paid. So if you feel comfortable hanging around at
more than Github go that way. Or infuse some great positive energy into the
world by supporting Github at their $7/mo level. And frankly, if you stop
paying them they don't take your private repos away. I'm sure it's a great PR
thing. They have my loyalty for life. 

Yay FOSS! Yay Linux! Yay Wikipedia! Yay Python! And Yay Anaconda and Jupyter
Notebook people and the whole linage of people behind vim (back to the line
editor). Anyhoo, a lot of stuff gets layered up, and I'm really digging living
at those lower levels that Steve Jobs symbolically "made the enemy" with the
Macintosh. User-unfriendly, one might say. One would be wrong. It's just a data
samurai sword for those who know how to wield it. 

And I spent A LOT of time learning how to wield vim, for which I am not for one
moment sorry. First vim, then emacs or the other direction Sublime Atom Visual
Whatever might float your boat. It's all cool, cause it's all vim emulation
everywhere. 

The only place I'm hard-wiring myself to vim would be in the loving gardening
of my .vimrc file over the years to unleash all the proper light energies for
the situation-- yet staying nearly default in all sane ways where you couldn't
recreate the spirit of your .vimrc in any other environment in a sitting or
two. So I think I'd be comfortable in nvim or neovim or maybe someday in emacs
in evil mode. But there is SOME hard-wiring here. It's a hard wiring to a sort
of text-navigation language... a LANGUAGE for editing text that leans into my
whole muscle memory data samurai hypothesis. 

I mean the vim bug has even bitten the hip Mac crowd. You should see some of
these totally Matt and Trey vimmers getting all verklempt over plugins. Hey
guys, real vimmers only edit their .vimrc's-- and not even all that much.
Prepare for life after vim. Long live vim! If you don't take the pluge, you
lack the sponge. Make the software portion of enabling you to express digitally
get encoded into your DNA. It needs a free and open source license. Don't code
anything you can't encode into your DNA license-free... that is if you really
want you and your descendants to own it long term. Is this Dune? Are we at Dune
already?

--------------------------------------------------------------------------------
## Thu Mar 22 

Okay, that out of the way. Now let's look at the real work-items for the day.
Be the data samurai you claim to be. The first few notes start:

    Jupyter Notebook
    Be deconstructionist.
    Re-create zero in your mind.
    When starting out, JN provides your zero.
    But only because OS implementations of ~/ vary.
    It sucks, but JN is your path to OS independence.

Don't bother pushing this stuff out to Twitter into Lunder-Vand, which they
don't even know yet is named that. Some day a "--Mike L" fan will discover this
here and go "oh! Premium really un-published content which is also fodder for
that book he's working on. And it's his even less filtered day-to-day thinking
as he hashes through a problem.

    When you get
    Started for the day
    You must reset zero point
    And if you can, you can do
    Most anything.

My zero-coordinate is increasingly becoming Jupyter Notebook, and I'm going to
have to advise that to my followers too. This is strange. It is not just the
generic browser itself that's home. It's a particular code-execution
environment (REPL) IN a browser, and really in Tab-0 or Tab-1 (more on that
soon). Neither is home really any more the ~/ "Home" conventional Unix/Linux
location despite how much I want it to be. It's just so easy to time:

    cd ~/
    
... as a method of clicking your heals together 3 times. You see? Unix/Linux
gives you a proper home. But because of pesky OS conventions that makes it
/home/username here and /Users/username in some other place, the host OSes
themselves sort of ruin this mostly in all other ways spiritually perfect
symbol-- almost root-- for "go home". But thankfully because this concept of
"home" is something Anaconda must decide each time it's run, you have SOME
flexibility, but trying to change it is setting yourself up for bugs and stuff.
Lean into Anaconda. Embrace the hug. It's going to have a Jupyter Notebook
launcher icon somewhere on the start menu or in applications. Run it and see
what location on your hard drive their default "home" is. It's almost certainly
the native OS's preference, which is most decidedly NOT ~/ when your Linux is
only a subsystem of a host Windows 10 OS. And no, it doesn't mean don't use
Windows. Mac's are fine as well as any self-respecting Unix distro (not
Levinux) with a GNOME or KDE desktop or anything Anaconda installs onto.

It is an important point that I have to keep bringing up that there's something
happening here.

I'm still in the final throws of settling in. Soon...

Most important thing now? 

Gotta get that crazy query corralled and all argument supporting. Make your
arguments to IT... not Boss. You've been challenged to rise to the occasion...
so rise!

The music is to fortify you against the background distractions. Shields up!
But check your email and calendar first. Standard dumbass avoidance. It's also
coming up on baking the donuts Friday. Get it out of the way Thursday. Don't
feel the crunch.

Don't think out loud too much, because you're going to publish. But it's safe
to say I've got tables to know. You've always got tables to know. It sucks,
but you always have tables to know. I can look in staging or live. Why not
staging where I won't be blocking? Sure, why not? And even there, it's a view
that you're dealign with and not a real table. It joins from 3 sources and is
large and intimidating to a guy like me who was stabbed in the back and
forsaken by SQL for it not having led me to sqllite years and years earlier,
and instead spoilt my taste for it completely, because... pile driver! I don't
need a pile driver. I need a hammer. If I wanted a pile driver, I'd have asked
for one. What? Now I have to dba the pile driver? No thanks. Databases are NOT
a welcome addition to your life in any way, whatsoever if you want to stay
samurai mobile. If you're gonna get bogged down, get bogged down with data
buckets of the sort of Amazon S3 or maybe MongoDB. Avoid tables. There's
religion and career-commitment to a sub-sub-speciality there just to be Kung Fu
effectiveness.

Enter pandas. I have to get pandas into fingers.

I'm switching my ACTUAL WORK over here to the new laptop to make myself
portable. Put on the Light Show on my main monitor. There are many other light
shows like it, but this one is mine. Show the heartbeat. Show the heart. Show
the green. Show the mean. BE what you advocate. Rain it gently down on those
around you. They'll be feeling it soon.

Step #1. Ingratiate. Be your affectatious self, but respectfully. Use your
laptop with the quiet keys when you can, but when you ARE working on the
work-provided computer (it's nickname is staticlenovo). It's been put in my
wide-screen multi-monitor configuration. And that means something OTHER THAN IT
as the 3rd screen off to the left usually (but I can do right) so that I've got
a 3-monitor system as spread out and taking-up of space as anyone around me,
even on a tiny desk. 

Remember, you've pretty much ALWAYS either got to be running the work-provided
VPN or HMA Pro because you either need access to the firewalled Amazon services
here at the office (or at home) over external networks like our guest wifi one
here that everyone uses. So remember if my database connection stops working on
my new machine, which I'm always walking around with, so it's all about running
the VPN for work... and at home at Urby Staten Island where I'm always on the
broadband down in the lobby. When I'm not cutting wires unlimited streaming
2-phone family-line 50GB unthrottled/mo T-Mobile style, I'm leaching off the
Urby wifi. Haha, can't wait for this journal to be discovered. Nobody's going
to know what to make of it. My phone keeps cycling on and off. Keep an eye on
it and make sure I've actually tested it.

Relax. Go look at the SQL. Just look at it. Exercise

Okay, I'm looking at the SQL. I'm not doing any relaxing... okay. Relax.

Data MASTER. I'm not that yet. This is the trial by fire stuff.

Get the barebones code that connects to Redshift. It's sitting in a file I'm
using every day. And in principle, you're just stepping into an existing SQL
statement changing a few things here and there. It's all just Python string
manipulations. I'm going to take the power of Python string manipulation to an
existing gobbledy

	q = '''SELECT Top 10
		blah,
		blah, 
		%s
		lots
		more
		stuff
		''' % 123

Okay, that works. But this is not the sophisticated type of string formatting
that I know is available these days. How does that go again? Google new python
string formatting... ugh, the exhaustive version is
https://www.python.org/dev/peps/pep-0498/ but the lite one is
https://pyformat.info/

Ooh, it looks like this:

    '{} {}'.format('one', 'two')
    '{1} {0}'.format('one', 'two')

Sexy, sexy. So you can pop them off a list OR use a sort of RegEx
back-referencing. Clever. That second one will definitely be it, because I'll
be using the same date-range over and over. And I have to DEFINITELY watch my
parenthesis. Incorrect order of operations would totally nuke this puppy, but I
don't see that much parenthesis in this. Okay, test the new format:

	q = '''SELECT Top 10
		blah,
		blah, 
		{1}
		lots
		{0}
		stuff {1}
		'''.format('one', 'two')

Okay, this is the marshalling. I'm going to have specific date ranges, which
are actually already created. There is another SQL statement. I'm going to be
looking for certain groupings where the URLs are found in a certain sub-set of
URLs. I need to filter that sub-set of URLs based on a bunch of conditions.

And now's when it gets real because I'm far enough along to work on the ACTUAL
query. This is where the rubber hits the road and sanitization no longer
possible in my notes. Peace out.

--------------------------------------------------------------------------------
## Thu Mar 22 

Joan. Pronounced Joe-ON. Remember it! This kind of shit is important, and you
call yourself a wizard. No, actually I don't. I aspire to be a wizard. I
partake of the wizardly arts and tools to do so, but I do not pretend 

Marshalling. Always be marshalling your forces. This desk-and-office location
both matters and doesn't matter routine is going to be hard to keep up if I
don't make it true, pronto. There is a lot of slack cut around here for
affectations, but I'm chock-full-o-affectations. I'm not sure if they're ready
for another Matt Downs, whose light-symbol of excellence I keep as a talisman
behind my abacus, which I keep around because you know, you never know.

Ohhhh, this is going to be interesting. The Surface Book 2 is for journaling...
personal journaling with timestamps and things. This is the way I type away
like a madman and don't bother anyone. I just paid about $3,000 (after warranty
and taxes) for a way to silence the one most objectively annoying affectation
about me-- my love for high quality mechanical keyboards, of the preferrable
buckling spring variety, but I like being reasonable and Cherry Brown will
suffice. I'm on the dasKeyboard Silent Pro, which is anything but silent. They
have renamed it since my purchase. Of course I'm publishing this. Labels are
important, and the way I've expressed it here really gets to the point of
everything.

    Money's not really important to me
    So, why not spend it
    On a top of the line laptop
    And get a lot more pleasure
    Out of all the individual little
    Now-moments that I'm trying to produce...
    ...Well, right now.
    In the Now.

In reply to someone on Twitter about URLs with no hate.

    While technically true and I do heart this
    There's a critical point that you cannot miss
    It's on the tip of my tongue... no need to send it
    The bell was rung. It's our Dearest #Amendment.
    by —Mike L
    #NewPoems for a #NewAge

On Martial Arts:

    Marshalling is working
    Though often looks like shirking
    I'll tell you why it's not
    Now listen up...

Johnny Stay Focused

    Let the real work begin...
    What? Huh? Oh.
    Yin emoters have no shield.
    Ugh! Color your sound.
    I need Apple.
    iPhone dead.
    Ugh.
    I'm no music person
    But those songs
    That playlist
    Apple's got me
    Until I make my
    Music cloud-mobile.
    Johnny B. Goode.
    He could filter out chatter
    Just like ringing a bell.
    

I think I'm going to take on the persona of a critically insightful Statler
Green Lantern, taunting the easily taunted with poetry that drops undeniable
but painful truths around indiscriminately like Anvils. If you happen to get
underneath one, sorry. Don't read what I write. It wasn't aimed specifically at
you, and I warned you I was doing this here. So you know, South Park disclaimer
and everything if you take any of this shit personally. I fling it freely and
take quite a bit of it myself, secure in my knowledge that you're just
British-emulating pompous asses and it quickly passes.

All I'm doing here is really just talking freely into my personal journal
anytime, anywhere. This is on my shiny new laptop that's like always on me now,
and carried around all the time, so who knows when an entry really went in...
so BAM free to publish the sanitized stuff. Wipe it off once and call it
sanitized.

I'm going to rock around the clock today.

--------------------------------------------------------------------------------
## Wed Mar 21 

Okay, I'm still going to "cut" journal entries, but now definitely it is to
label the posts. I have a macro @j set up to create a new journal entry. So...
so, get that email to your boss out to let him know you're working from home
and that all is well. Make sure all is well, and that on work VPN you can hit
Redshift... running query. As soon as CSV's appear, my answer is a-ok! A-OK!
Pshwew! Send email... done. Okay. Think EVERYTHING through.

Don't feel like you're going to push everything here out to Pipulate's leaky
journal. You're not. Write freely. Don't inhibit yourself. Strategize when and
how you must. This is your safe place, which even if it leaks someday won't
cause you too much grief, but in the meanwhile isn't going anywhere online
that's supposed to be accessible to anyone. But like Github's secure.

Okay, now that it's confirmed, let's do some serious shit here. Go back to HMA
and start pulling down files locally you want to get off the Microsoft Cloud.
That's gone on long enough. Consolidate on Google and make Microsoft 360, even
at their $60 level, optional. Everything about Microsoft now should be optional
except taking advantage of some killer hardware and a decent embedded Linux
sub-system. Don't hold it against the hardware that what we call Windows 10 is
up there in control. There's a word for that sort of stuff. It's called a
driver. Windows is now a driver for Chrome (or Chromium if you prefer) browser
and the Hyper.is Unix Shell terminal program built on Electron, which is a
re-porpoising of Chrome components... so tight. Tite. All round.

-------------------------------------------------------------------------------
## Wed Mar 21 

Well, here we go. A new work location, a new laptop, a new mission in life and
view on the world, and definitely a new attitude.

Installing HMA Pro! VPN (Hide My Ass) so that when I'm not on the office VPN, I
can be here on my own at Urby, where the WiFi is open and the passwords are
a'flying. I've got to talk to them about that. The proper way to do this is to
have a secure WiFi network and freely advertise the password. With all this
decoration around the place, they could use framed password art and it would
still be more secure, because at least then the network traffic would be
encoded. Same with the Subway. Sheesh, people! Just because your browser and
most websites these days are using are using SSL security (thank goodness), not
EVERYTHING is secured, like cookie data in the request headers, which just
might carry a hijack-able token. People, don't use open WiFi without
protections. Services like HideMyAss are only like $60/year and have so many
local end-points these days, the slow-down of your surfing and even streaming
is hardly noticeable.

Wow, having color coding turned on in markdown really does make a nice little
difference in the journaling process. Looking at even just a little bit of
color adds some sort of emotional content. I get it. Don't know if I like the
colors, but at least I'm being made aware I need to think about it. Also,
without the wide-format 16x9 HDTV format of desktop monitors where side-by-side
terminals are preferrable because you have plenty of horizontal space to work
with, on a laptop like this I need to choose between 80-columns nearly filling
up my whole screen (zooming-down occasionally for wide-format programming), or
looking at tiny energy-sapping fonts all the time, reproducing the side-by-side
80-column configuration I used when in "static mode" sitting at my desk.

Oh, God, muscle memory is important. And no, I'm not using the Lord's name in
vain here. Muscle memory is one of God's true gifts, and so denied to us in
everyday tech. Okay, so HMA is done installing, and I quite the work-provided
VPN and am trying my own. It connects. Using HMA Fast Mode, because who cares.
This is not for anonymous surfing from anywhere in the world, though I'll talk
plenty about that later. Rather, this is about just a minimum bit of protection
against identity theft on public open networks shouldn't be such a thing,
people COME ON! Okay, Google pushing all websites into end-to-end security
helped, but hijacked cookie tokens and stuff. Use protection.

--------------------------------------------------------------------------------
## Tue Mar 20 

Okay, that was interesting. Next? Okay, the big project for today. It's still
about those revenue columns. Wow, that was a bigger project than I expected.
Okay, hit home the going back a whole year thing. But definitely be cognizant
of the fact that you now want to REGULARLY push out Pipulate and PrivateJournal
commits together before you leave at the end of the day. There will ALWAYS be
changes to pipulate now too.

That's all about just sitting and looking at the existing SQL that makes the
join and understanding how I would go about turning that into a filtered
sub-set of that view, applying both:

- The date-range filter (in several places and switching to dual-boundary)
- The chained-up URL where condition that will have (ooo) issues.

Wow, with this new datestamp situation, there's no longer to start a new
journal entry. The whole idea of CUT! is gone. Just gone. And I think I may
like it better this way. It takes off a lot of pressure. This is the test of
whether... yep. The .vimrc change took. Good. It will be nice to have
color-coding in my markdown file in vim now that it doesn't need to have a
.html extension for my old... what was it? Strapdown.js, I think. It was a very
good method for its day to push this out for every-day consumption where I
could use what was it? Hotbox? To watch people read my journal from all over
the world. Ah, those were the days. But alas, no. Now you read this shit
through Github in the miklevin/Pipulate repo, or nowhere. Good luck, haha! I
don't need no stinking voyeuristic JavaScript. There are more important
Noosphere eggs to be frying. Let's get to one.

I actually want to associate this challenging new in-Jupyter Notebook SQL work
that I'm doing with my new laptop. My goal is to be able to go home tonight,
and through both VPN and a repo-less way of transmitting simple sample code for
Jupyter Notebook around, be doing this "revenue column" work. I'm basically
joining tables from all over the place. But what's worse, I'm reaching for some
really valuable data that has all sorts of challenges in reaching... hmmm,
yummy and perfect! Okay, I've got this. No problem.

Problem is, I'm changing floors at work and I generally do my best work... Ah,
switched. I was going to say on a loud keyboard, but I couldn't bring myself to
type it so loudly. When it's quiet here, switch to the laptop. 

Wow, always having 2 journals loaded, now with the first named journal.md and
the second named leakyjournal.md is a real kick, let me tell you. How such an
obvious and uber-techie solution to pushing out sanitized private journal
excerpts was so obvious and right under my nose for all this time makes one of
the important points I want to make in this book (the book that this is going
to be source data for) is that light touch solutions are almost always there.

Light touch has got to be one of my catch phrases for all of this Alice in
Wonderland tech analog book I'm making. Wow, things are falling together. Did
you buy the wrong hardware or take up the wrong language years ago, and somehow
feel committed to sticking with it, even though it's draining your soul? Well,
good for you! Dynamic growth is scary, and isn't for everyone. Me? Let me keep
bearing down on this Linux, Python, vim and git track. It's a good one.

But portability of Jupyter Notebook like copy/paste locations that can be
shared between machines... and maybe even...

--------------------------------------------------------------------------------
## Tue Mar 20 

    let @j = '/Bginning of Journal^Mo^M^M^M^M^[kkkk80i-^[j! date^Mi## ^[^Mjzzi'

...becomes:

    let @j = '/Bginning of Journal^Mo^M^M^M^M^[kkkk80i-^[j! date^MwwwD0i##^[^Mjzzi'

It's really that simple. Changed highly detailed timestamps from the Unix
(Linux, of course) "date" command from highly detailed to just:

    Tue Mar 20

...with the addition of:

    wwwD0

...somewhere into a macro, which I keep in a .vimrc file, which I keep in a
repo called vim in a public github repo so that I can pull it down from
anywhere, get the idea?

As an added bonus, if I leave my cursor at the top of the pipulate version of
the journal, when I switch to it with a :bn (for buffer, next in vim-speak) I
know just hitting the p for paste and then saving it, and then going back to
the top of the document and hitting :bn again sort of "stages it" both to be
published on the next inevitable commit and push of changes to the Pipulate
project from this machine, but it's also staged for the very easy publishing of
my next bit of stuff. No fancy system-building. Just one file in
/usr/local/sbin so that every time I open a new terminal, I can just type:

    j[Enter]

...and have both journals loaded for easy permission-controlled publishing, yet
all from just vim and git. No graphical OS really even required here. This is
less than wristwatch-level power you're requiring here to host your
journal/publishing system... for life. Just add Internet connection and common
free stuff.

--------------------------------------------------------------------------------
## Tue Mar 20 11:06:48 DST 2018

Okay, I have a lot to do today, but first it's time to eliminate accurate
timestamps in my private journal macro. It's been attempted to be used against
me even one little bit, so it's gone. But none of the actual benefits of the
journal itself will be gone. Nope, rather my loud and very distinct inner voice
is going to not be talked-over, and it's going to go, yup. Solution provided. I
control the timestamps. I control the reality. Timestamps are only as accurate
as the day's date. Morning, night, who knows? There's some sense of linear
sequence, but I think out loud a lot on my lunchbreak and on the subway now
with my Surface Book 2 laptop, where I can work anywhere quite well to be
always-there, always-on and at my own expense for the best laptop in the world
right now available-- although middle-of-the-line, because I'm not made of
money. I just like my tools. And I think I need to assert myself from time to
time to keep this situation and the opportunities here viable, and me free off
all the signs of burn-out that have already set-in after just 2 years. Nope.
Fix or leave. Fixing begun. Timestamps...

--------------------------------------------------------------------------------
## Tue Mar 20 

Beginning of... oops can't type that or I'll mess up my Macro. Time to get
a'crackin'. My mission today is this SQL Query thing to go back a year ago in
revenue numbers... wow! I should of done that yesterday... or maybe even
Friday, but wow. The office move, the new laptop freeing me to work anywhere,
and all the settling in, which is... oh, let me tell you about it! But wow, can
I do some cool samurai data moves on that thing now. I need a more full-time
built-in WiFi, and I was hoping for... wait! I'm going to publish this. I know
that. This is a critical part of the Datamaster journal-- calibrating one's
tools for maximum effectiveness under all the conditions you're likely to find
yourself in. For too long, I've used old Mabook Airs... 3 of them, to be
precise, haha! I have 2 now still myself. Gotta set Adi up on one, but they're
so old-school: no touch-screens and high-res artist's stylus. What's that you
say? Neither do modern Macs? You've got to be kidding, that's got to be a
joke... what? At least their Phablet has a Stylus so that Differently Thinking
Artists can... what? No stylus, either? What happened? Does Apple still
exist... oh, a consumer goods company yous say? Maximum profitability, sheep,
Jobs is dead and all that? Okay, got it. Still wearing my Apple Watch and
making the SE my wallet-phone. The NYC 212-NYB-1337 number is getting ported to
the Note 8, because I needed a phone-number as cool as everything else in my
life, now that my transplanted roots are really beginning to set in... here...
in New York City, where I live with the best view of it right on the edge of
Staten Island. I've finally gone UrbyLife.

Okay, I still have a little publishing resistance because there are some
annoying kung fu keyboard moves of loading another file on a different path
into the second vim buffer. I can totally do it, but I'm fatigued just thinking
about what that would take. 

    The light! The light! 
    The lite, the lite, the lite.
    So, fight! So, fight! 
    And fight and fight and fight.

Even on this floor, there will be big-time mental distractions. The sound of
your inside voice has to be as loud as the chatter, or else people won't
realize their chatter is a part of your background noise while you're trying to
work. That's okay. That's the cubicle deal. People type, and I'm using a very
high quality keyboard, thank you very much. And I shouldn't HAVE TO try to
drown it out with headphones blasting music into my head, and I'll damn-well
talk about it as a focus and survival strategy for creatives in the cubicles of
modern business, readily. It's a fine topic to discuss, especially at the very
moment it's an issue, and you need something as your ohhhhm to regain center,
and get back to some important work.

Okay, there.

Now where were we?

Oh yes, make it so that publishing this will be nice and easy from here on out.
And that means either a something.sh in your current directory (which you'll
never be quite sure you're in) or putting it somewhere in your path, and
chmod'ing it to have +x permissions (execution). So, this is your second step,
because it is true, everything is a LITTLE BIT difficult. They used to joke
about Unix that that was intentional to make an elite class of techs, and well
yeah, sorta. It's called smart enough to appreciate inside jokes, and it's
important in the Unix world, which WAS a priesthood even though its progenitors
were badboys, because of the great commercial and proprietary potential of Unix
to vendors like AT&T... and Novell... and SCO. Oops, proprietary was something
special, was it? Not when it's the commodities, and basically free because it's
only already-ripped-off data, because it's digital data. Blackbox copying has
inconsequential cost, which is what Linux and RMS did. So...

So, bash shortcuts in sbin. Sbin is a funny thing. It's supposed to be these
tiny little one-off script files that you plan to use a lot, and they're still
usually script or bash or shell files. They're all sort of the same since bash,
the "Bourne-again shell", became so durn popular. It's got to be more than just
the basic vanilla Unix "shell" with no command-line history or completion, so
everyone at least uses the first mega-popular one that nothing else ever quite
displaced. So, the language flavor of Unix scripting you should be using is
bash, and they usually just have a .sh extension for shell.

Okay, getting there might take a little while but the payoff is enormous. This
entire seeing the sausage factory process of permanently improving my
day-to-day workflow is being exposed here in the Pipulate repo for everyone to
see... haha! But the world is different forever once achieved. Everything
hinges on moments like these, such as the next time I want to publish like this
won't be anywhere near as difficult.

Keep my go/zd gnu screen session going that shows my every 10-minute heartbeat
after the daily regimine of scripts stops running... or really is just paused
waiting for later in the day when the speed-checks begin, so it gets a fair
assessment of the speeds of different sites (can't run that during the night).
But that report will probably be changing now that Google has an site speed
check now for almost precisely the same scorecard type thing. So much I can gut
and take a sawzaw to, and build newer better stuff to replace it... easily and
more easily than maintaining the old stuff, and that's like one of the big
points about having an employee like my. My stuff is only built to last for
about a year until realities change. Lean into that. Allow scrap and rebuild to
occur, but don't keep me playing little dutch boy and the dike. If a dam's
going to bust if left unchecked and I've said so a lot, then I'm just going to
let it bust. I'm not paid enough to keep old dams from busting AND building new
ones. That's a losing proposition, so I've got a plan.

That plan is sbin.

Gotta always remind yourself of the location. 

It's an odd incantation, but this is it:

    echo $PATH

9 times out of 10, it's going to be /usr/local/sbin and it's going to be the
first thing in your path. Understand that, and you're going to understand a lot
about Unix and Linux. The next step, I'm going to tell you to do in vim as your
frustrating and fateful first encounter with the big green monster. Wanna be a
badass tech always packing sharp quarrels in your quiver that'll really make
'em shiver when they see the kind of tech who is really good as heck. Oh, I
don't even need a .sh extension.

    sudo vim /usr/local/sbin/j
    :i
    vim /home/journal/index.html /mnt/c/Users/whome/github/pipulate/theleakyjournal.md
    [Esc]:wq
    sudo chmod +x /usr/local/sbin/j

Left out some details like how you should hit enter. Wave. Quit... tested! Wow!
Now, go publish this shit.

--------------------------------------------------------------------------------
## Fri Mar
### Getting down the rhythm of the Pipulate workflow

You lost the flow. Time to re-establish. These things are taking you wayyyy
longer than they should. I've got idea... I'm going to change my vim macro to
only give the day in the timestamp... hahaha! Only the day is important to
anyone who lacks the ability to see when the git commits occurred-- hahaha!
Wow, I've become a tech asshole. You people have to watch me. I really don't
want to become what I hate, those Green Arrows can eat my Blue Beetles. But not
until after the work-and-hand is done. So far, we have...

- Templates are for purple cows
- Whipping docs get nuked for morbid
- Copy from a Pipulating GSheets (create consistent compelling language here)
- Copy from the Purple Cow farm.

Now, you've got Whipping Doc with no more tabs than what you absolutely need...
not quite true. One blank sheet may still be in there, which you can delete
because you don't need anymore.

Good language developing: "Oh yeah, that's a pipulating sheet. Don't reorganize
those columns (or do) because that's pipulating live. It's a pipulating live
pipulating sheet. Don't pipulate with me, I'll pipulate your pipulate.
Recursion limit reached."

Okay, recover state...

- NOW ADD NEW TEMPLATE COLUMNS INTO LOCATION

Ah, Newspace! A purple cow in the cow farm need not a column or row more than
it need. It should indeed be pruned so you can click the copy-whole-spreadsheet
magical place in all spreadsheet software. That is VERY GOOD. This is the sort
of non-system system invention that Pipulate should be built from. Just know if
you do these such-and-such obvious-in-hindsight things (trimming unnecessary
rows and columns) everything will go more smoothly in your Pipulate workflow...
something that is very worth getting worked-out just-so because of the
effortless mastery things like fixed-position brings to them over time. Every
fixed position where you can re-acquire home and recalibrate and regain state
real quick is a treasure.

Newsflash: Conditional formatting doesn't copy-paste even with "Paste special"
between sheets. Consequently, there's definitely got to be a lot of
right-clicking on tabs to "copy them into" other sheets. That seems to preserve
it, but there's none of the required formatting in my Purple Cow Farm template
tab, which I realized late in that project. And I fixed it in the Whipping Doc,
but I have to copy it back from the Whipping Doc to the Purple Cow Farm... wow,
this is going to work.

Okay, confirmed. Copying sheets through GSheet's "Copy to" on the Tab's menu
preserves the conditional formatting... pshwew! Purple cows can stay purple.
Oh, always color-code a the tabs in The Purple Cow farm purple... color coding
is going to be some powerful stuff in this non-system system.

--------------------------------------------------------------------------------
## Fri Mar

Okay, when doing new work, the work-rhythm looks like this:

Make sure the Purple Cow Farm has your template checked-in (so to speak).

Nuke your whipping-doc for morbid. Know 2 things are about to be zapped into
there. You are merging 2 source-documents:

- Your live-deployed GSheet that's back-ended by "scheduled" pipulate.
- Your template from the purple cow
- Copy-to Recent from the "Tab" menu in GSheets is going to be a common thing.
- Once a tab is copied that way, it gets renamed to "Copy of [Old sheet name]"

--------------------------------------------------------------------------------
## Fri Mar 16
### Blank The Whipping Doc for Morbid. It's the only way to be sure.

Okay, now down to business... again. And this time for real. This is very
serious business. But my distractions were in forming a very focused mental
model for this type of work today and FOREVER FORWARD MORE IMPORTANT THAN IT
LOOKED distraction. Tired of leaping for peanuts.

Speaking of speaking my mind. I know it's probably politically incorrect, but a
WORK-IN-PROGRESS document is a whipping doc. It's got a very powerful concept
there. You can blank the whipping doc. It is wise to blank the whipping doc, in
fact because if you have a Purple Cow Farm with your format in it, All other
instances than what's live in-scheduling will just muddle don't force a rhyme.
vim out!

--------------------------------------------------------------------------------
## Fri Mar 16 
### If I Saw a Purple Cow, I'd Pick Out a Good Nickname

Time is an illusion. Okay, Purple Cow Farm in-hand, we have a solid "from"
place, once our template-work (sculpting light) is done in whatever, wherever
format woo hoo everything-independent where we can be. We copy all that
artistic header-area stuff of the WORK-IN-PROGRESS document (anything, anywhere
like Excel or another GSheet) into the Purple Cow document. You ALWAYS include
the first data-row, which is the row usually immediately below your frozen
title rows. There's some ambiguity around what we call this area, but I'll use
header for consistency with typical office-speak. So, we put the complete
header and first data-row into its own tab in The Purple Cow Farm. Things line
Red/Green color-coding rules get carried in that first data-row, so it's really
important. I wouldn't try blanking the data in there, or you're in for all
sorts of accidental formatting-loss issues. Just assume all the data in Purple
Cow is for-position-only (FPO). Okay... now we have a destination document.
It's where we "blend into" and should be the SAME as your work-progress
document, so you don't have to be giving out new Google Sheet URLs all the
time. Even the SEO in me screams out no to that concept. WIP (work-in-progress)
documents should get good strong nicknames and have a long life as such a
kooky-nicknamed thing... until you rename it for a demo to a stakeholder who
doesn't need to see it by that name. But then, it's almost an inside joke that
it's really the such-and-such document, because you've touched them on an
emotional level with a just-so-perfect nickname...

And that my friends is SEO. Walk the walk so you can talk the talk... be DEEPLY
engaged in the game by partaking in all the plentiful Noosphere being created
by every move Google makes... every step it takes, we'll be... oh wait, it's
watching us... nevermind.

--------------------------------------------------------------------------------
## Fri Mar 16
### Just Invented Purple Cow Farms for Templates

I just hit on a very, very powerful method. Why just use one journal in vim
when you could be using two! One of them in a private git repo and the other in
a public Github repo, but with no special effort taken to format or publish it,
besides naming the file with a .md extension and putting it in the parent
directory of a repo I think I'll be driving a lot of eyes to and think I'll be
able to turn this into a good lesson in iron bars to not a prison make nor
cubicles a circus. Minds both intent and focused can still squeak out a
workplace. As non-technical people suspect and sometimes fear, the shell-game
in doing very advanced-seeming stuff in tech requires a lot less actual work
than what it appears. But that cover of being busy and stressed-out and always
intently working on something is very important. Mechanical keyboards that you
can feel click under your fingers is important too. Get into the zone whatever
way you can, and if that means throwing up a shield of better not interrupt,
then so be it. 1, 2, 3... 1? Templates are PURPLE! MAKE YOUR PURPLE TEMPLATE
DOCUMENT. A purple cow farm. HAHAHA! You sometimes look for the proper amount
of ridculoustemity in your nicknames. Ohhh, push this out.

1, 2, 3... 1: Go find your Purple Cow.

--------------------------------------------------------------------------------
## Fri Mar 16

    Different rhymes for different times
    And if you don't renew 'em
    From time to time, you'll fail to climb
    And fall down in a ruin.

    Purple is for templates now;
    The other colors taken.
    Make them be your Purple Cow
    To never be forsaken!

    I've only got one document
    That's named The Purple Cow Farm;
    Templates-tabs-- from there are sent
    With minimum of brain-harm.

    The Purple Cow will teleport
    The columns where they function
    While you try to stop a fork
    Off version we be junkin'

--------------------------------------------------------------------------------
## Fri Mar 16 

Make donuts. 1, 2, 3... 1? Source Templates! It's all about reflecting the
right light with the proper incantations. Everything will shine through your
Google Docs templates, which you really should set up ahead of time, because
although you CAN apply some formatting with PyGal which apparently doesn't use
GData but something else more formal under the Developer Console (GData is so
old it predates API-unification under-console). I need to get this stuff out,
because it's important about Pipulate. Getting started on a project in the
morning where ambitions are high because they realize the: if Data Samurai,
then following views we've never before been able to consistently:

- produce
- make readily/easily available
- yet still secure the data

...that one would thing should easily be possible. It's not. But I'm here to
solve that. You're gonna have to drink some Koolaid, so ya had better get used
to it. What, you think Google is going away? What, you think the search game is
going to be disrupted because of some AI-startup? Forget it. A 10x early-mover
advantage in this game is exponentially more than you think. Thinks are
learning and those learnings are persisting and trickling out all over have its
input improved from all over the place... not human by a long-shot, but a damn
bigger chasm that newcomers need to cross than you can imagine.

So, why even try.

Different game, lads. I'm in a different game, with what I hope is another 20
years of exploi... ahem, exploration left to do.

Forget the #xbook tag. Just publish in the Pipulate repo. This is what you were
born to do. vim out.

--------------------------------------------------------------------------------
## Fri Mar 16 

I'm just kidding. I won't leak. But I'll probably sanitize as I type so that
when I copy/paste daily journal entries over here, I won't have to do much
editing. Consider this a history with the most recent thoughts posted as an
entry at the top. Let's make up a word for this... oh, it's on the web, and
it's a log. I know! Let's call it a blog. And here's my first copy/pasta...

--------------------------------------------------------------------------------
## Fri Mar 16

1, 2, 3... 1? List.

You will have various 1, 2, 3... 1? List's in your life.
https://docs.google.com/spreadsheets is one

This is because Google Sheets is 80/20-rule good enough. And I will go into
that a lot more soon. In the meanwhile, I'm thinking to myself how this gets
published and pushed out in a reasonable way, and I'm thinking to myself, the
Pipulate repo, dumbass! There's going to be some eyes on that thing, and this
maybe forever forward in the quite interesting by now never-rebased but
definitely should have been but keeping it that way for more badassitute oughta
watch my mouth paid my dues on Jupyter Notebook now and appreciate what I've
got because... Flask version of Pipulate... OMG! I needed nested bubbling
yields used generically through Pipulate-compatible functions if you wanted
that twinkling UI-feedback that could be sent on the same response that was to
the original page-request, just don't stop building the page and use that no
ajax webserver tech required cause it all uses the highly compatible magical
capabilities of modern browsers to pull it off no JavaScript libraries required
genuingenuity. BAM. Should'a started that project on Python 3 where yields
actually could nest and bubble. Oh, but the complexity, and the trap had it
really worked well... would not be on Jupyter Notebook today really
appreciating it for the miracle the iPython and Continuum.io people really
pulled off there.

Okay, that was my "I am a true Samurai-repurposer of tech once I've aquired it
old'skool real. Oh there I go again with hyperbole. See! I can't even just say
hype. Well, that's me. Welcome to full-on corny nerd. And it's going in right
here, because performance art. Bust-out-ittude and other crazy made-up SEO
words because that's it. I'm an SEO. I'm here to walk the walk while I talk
the talk, and if you're not out here doing something interesting on Github,
then you're not out here. STOP! Reports checked. Now, bake donuts. Recover this
state. It is important. vim out!

--------------------------------------------------------------------------------
## Fri Mar 16 

It's time to bake the donuts.

No, first check the reports!

And get into the mindset of santizing this again as you write, timestamps
removed of course in a time-displaced published version... who knows when this
occurred unless you're reading over my shoulder. Oh, permissions and
securities, and the philosophy behind your thoughts truly being V for Vendetta
versus eventually enough on the Cloud... well, whatever.

For now, we check reports then bake donuts... then stop and survey the
landscape.

- What's most broken?
- Which work gives us the most bang for the buck?
- What plates need spinning (think about 3rd or else there goes your day)

--------------------------------------------------------------------------------
## Thu Mar 15 

Might as well be on the best. I want to be on the best hardware of my life
while I'm doing the best work of my life.


