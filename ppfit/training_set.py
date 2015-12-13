import numpy as np

class Training_Set:

    def __init__( self, configurations ):
        self.configurations = configurations
        self.forces   = np.concatenate( [ c.reference_forces   for c in configurations ] )
        self.dipoles  = np.concatenate( [ c.reference_dipoles  for c in configurations ] )
        self.stresses = np.concatenate( [ c.reference_stresses for c in configurations ] )

    def run( self ):
        for c in self.configurations:
            ran_okay = c.run( clean = True )
            if not ran_okay:
                return( False )
        return( True )

    @property
    def new_forces( self ):
        return np.concatenate( [ c.new_forces for c in self.configurations ] )

    @property
    def new_dipoles( self ):
        return np.concatenate( [ c.new_dipoles for c in self.configurations ], axis = 0 )

    @property
    def new_stresses( self ):
        return np.vstack( ( c.new_stresses for c in self.configurations ) )


