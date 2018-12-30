def rk4 ( t0, u0, dt, f ):

  f1 = f ( t0,            u0 )
  f2 = f ( t0 + dt / 2.0, u0 + dt * f1 / 2.0 )
  f3 = f ( t0 + dt / 2.0, u0 + dt * f2 / 2.0 )
  f4 = f ( t0 + dt,       u0 + dt * f3 )
#
#  Combine them to estimate the solution U1 at time T1 = T0 + DT.
#
  u1 = u0 + dt * ( f1 + 2.0 * f2 + 2.0 * f3 + f4 ) / 6.0

  return u1

def rk4_test ( ):
  import numpy as np
  import platform

  print ( '' )
  print ( 'RK4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RK4 takes one Runge-Kutta step for a scalar ODE.' )

  print ( '' )
  print ( '          T          U(T)' )
  print ( '' )

  dt = 0.1
  t0 = 0.0
  tmax = 12.0 * np.pi
  u0 = 0.5

  t_num = int ( 2 + ( tmax - t0 ) / dt )

  t = np.zeros ( t_num )
  u = np.zeros ( t_num )

  i = 0
  t[0] = t0
  u[0] = u0

  while ( True ):
#
#  Print (T0,U0).
#
    print ( '  %4d  %14.6f  %14.6g' % ( i, t0, u0 ) )
#
#  Stop if we've exceeded TMAX.
#
    if ( tmax <= t0 ):
      break
#
#  Otherwise, advance to time T1, and have RK4 estimate 
#  the solution U1 there.
#
    t1 = t0 + dt
    u1 = rk4 ( t0, u0, dt, rk4_test_f )

    i = i + 1
    t[i] = t1
    u[i] = u1
#
#  Shift the data to prepare for another step.
#
    t0 = t1
    u0 = u1
#
#  Terminate.
#
  print ( '' )
  print ( 'Rk4_TEST:' )
  print ( '  Normal end of execution.' )
  return

def rk4_test_f ( t, u ):

  import numpy as np

  value = u * np.cos ( t )
  
  return value

def rk4vec ( t0, m, u0, dt, f ):

  import numpy as np
#
#  Get four sample values of the derivative.
#
  f0 = f ( t0, m, u0 )

  t1 = t0 + dt / 2.0
  u1 = np.zeros ( m )
  u1[0:m] = u0[0:m] + dt * f0[0:m] / 2.0
  f1 = f ( t1, m, u1 )

  t2 = t0 + dt / 2.0
  u2 = np.zeros ( m )
  u2[0:m] = u0[0:m] + dt * f1[0:m] / 2.0
  f2 = f ( t2, m, u2 )

  t3 = t0 + dt
  u3 = np.zeros ( m )
  u3[0:m] = u0[0:m] + dt * f2[0:m]
  f3 = f ( t3, m, u3 )
#
#  Combine them to estimate the solution U at time T1.
#
  u = np.zeros ( m )
  u[0:m] = u0[0:m] + ( dt / 6.0 ) * ( \
            f0[0:m] \
    + 2.0 * f1[0:m] \
    + 2.0 * f2[0:m] \
    +       f3[0:m] )

  return u

def rk4vec_test ( ):

  import numpy as np
  import platform

  print ( '' )
  print ( 'RK4VEC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RK4VEC takes one Runge-Kutta step for a vector ODE.' )

  n = 2
  dt = 0.1
  tmax = 12.0 * np.pi

  print ( '' )
  print ( '          T          U1(T)            U2(T)' )
  print ( '' )

  t0 = 0.0
  i = 0

  u0 = np.zeros ( 2 )
  u0[0] = 0.0
  u0[1] = 1.0

  while ( True ):
#
#  Print (T0,U0).
#
    print ( '  %4d  %14.6g  %14.6g  %14.6g' % ( i, t0, u0[0], u0[1] ) )
#
#  Stop if we've exceeded TMAX.
#
    if ( tmax <= t0 ):
      break

    i = i + 1
#
#  Otherwise, advance to time T1, and have RK4 estimate 
#  the solution U1 there.
#
    t1 = t0 + dt
    u1 = rk4vec ( t0, n, u0, dt, rk4vec_test_f )
#
#  Shift the data to prepare for another step.
#
    t0 = t1
    u0 = u1.copy ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'RK4VEC_TEST:' )
  print ( '  Normal end of execution.' )
  return

def rk4vec_test_f ( t, n, u ):

  import numpy as np

  value = np.array ( [ u[1], - u[0] ] )
  
  return value

def rk4_tests ( ):

  import platform

  print ( '' )
  print ( 'RK4_TESTS:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the RK4 library.' )

  from rk4 import rk4_test
  from rk4 import rk4vec_test

  rk4_test ( )
  rk4vec_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'RK4_TESTS:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  rk4_tests ( )
  timestamp ( )

