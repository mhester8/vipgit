from ase.io import read
from espresso import espresso
from ase.optimize import QuasiNewton

name = 'pt'

slab_ads=read(name + '.traj')
slab_ads.calc=espresso(pw=400,
                       dw=4500,
                       kpts=(6,6,1),
                       xc='PBE',
                       outdir='E_slab_ads',#espresso outdirectory saved
                                            #here                                    
                       convergence={'energy':1e-6,                                                 
                                    'mixing':0.05,
                                    'mixing_mode':'local-TF',
                                    'maxsteps':1000,
                                    'diag':'cg'})

relax_slab_ads=QuasiNewton(slab_ads,
                           logfile=(name + '_opt.log'),
                           trajectory=(name + '_opt.traj'),
                           restart=(name + '_opt.pckl')) #ase output
relax_slab_ads.run(fmax=0.05)

E_slab_ads=slab_ads.get_potential_energy()

print(E_slab_ads)
